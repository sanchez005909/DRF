from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView

from payments.models import Payment
from payments.seriallizers import PaymentSerializer


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer


class PaymentListAPIView(ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # search_fields = ['curs', 'lesson']
    filterset_fields = ('curs', 'lesson', 'payment_method')
    ordering_fields = ['date_payment']
