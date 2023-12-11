# from django.urls import path
from django.urls import path
from rest_framework.routers import DefaultRouter
from curses.apps import CursesConfig
from curses.views import CursViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

app_name = CursesConfig.name

router = DefaultRouter()
router.register(r'curses', CursViewSet, basename='curses')

urlpatterns = [
    path('lesson_create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson_detail/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-detail'),
    path('lesson_update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson_destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-destroy'),

    ] + router.urls

