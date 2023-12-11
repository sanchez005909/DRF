from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, \
    UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    # user
    path('user_create/', UserCreateAPIView.as_view(), name='user-create'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('user_detail/<int:pk>/', UserRetrieveAPIView.as_view(), name='user-detail'),
    path('user_update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('user_destroy/<int:pk>/', UserDestroyAPIView.as_view(), name='user-destroy'),
    # token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
