from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from curses.models import Curs, Lesson, Subscription
# from curses.permissions import IsModerator
from curses.permissions import IsOwner, IsModerator
from curses.serializers import CursSerializer, LessonSerializer, SubscriptionSerializer


class CursViewSet(viewsets.ModelViewSet):
    serializer_class = CursSerializer
    queryset = Curs.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_curs = serializer.save()
        new_curs.owner = self.request.user.email
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
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]
