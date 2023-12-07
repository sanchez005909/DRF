from django.urls import path
from rest_framework.routers import DefaultRouter

from payments.apps import PaymentsConfig
from payments.views import PaymentCreateAPIView, PaymentListAPIView

app_name = PaymentsConfig.name


urlpatterns = [
    path('payment_create', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payment_list', PaymentListAPIView.as_view(), name='payment-list'),
    ]

