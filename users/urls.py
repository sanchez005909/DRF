from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, \
    UserDestroyAPIView

# from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserDestroyAPIView, UserUpdateAPIView

app_name = UsersConfig.name

# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('user_create/', UserCreateAPIView.as_view(), name='user-create'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('user_detail/<int:pk>/', UserRetrieveAPIView.as_view(), name='user-detail'),
    path('user_update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('user_destroy/<int:pk>/', UserDestroyAPIView.as_view(), name='user-destroy'),
    ]
