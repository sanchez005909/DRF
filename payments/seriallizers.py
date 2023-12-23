from rest_framework import serializers

from payments.models import StripeCheckoutSession


class SessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StripeCheckoutSession
        fields = '__all__'
