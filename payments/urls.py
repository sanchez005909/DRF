from django.urls import path

from payments.apps import PaymentsConfig
from payments.views import StripeCheckoutSessionCreateAPIView, StripeCheckoutSessionRetrieveAPIView, \
    StripeCheckoutSessionListAPIView, StripeCheckoutSessionDestroyAPIView

app_name = PaymentsConfig.name


urlpatterns = [
    path('create_session/<int:pk>/', StripeCheckoutSessionCreateAPIView.as_view(), name='create_session'),
    path('session_retrieve/<str:stripe_id>/', StripeCheckoutSessionRetrieveAPIView.as_view(), name='session_retrieve'),
    path('session_list/', StripeCheckoutSessionListAPIView.as_view(), name='session_list'),
    path('destroy/<int:pk>/', StripeCheckoutSessionDestroyAPIView.as_view(), name='destroy'),

]

