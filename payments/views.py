from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView

from payments.models import Payment
from payments.seriallizers import PaymentSerializer


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer


class PaymentListAPIView(ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()