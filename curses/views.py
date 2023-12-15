from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from curses.models import Curs, Lesson, Subscription
from curses.paginators import CursesPaginator
# from curses.permissions import IsModerator
from curses.permissions import IsOwner, IsModerator
from curses.serializers import CursSerializer, LessonSerializer, SubscriptionSerializer
from users.models import User


class CursViewSet(viewsets.ModelViewSet):
    serializer_class = CursSerializer
    queryset = Curs.objects.all().order_by('id')
    permission_classes = [IsAuthenticated]
    pagination_class = CursesPaginator

    def perform_create(self, serializer):
        new_curs = serializer.save()
        user = User.objects.get(email=self.request.user.email)
        new_curs.owner = user
        new_curs.save()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated & ~IsModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CursesPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]
