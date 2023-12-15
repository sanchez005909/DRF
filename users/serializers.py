from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'role', 'email', 'phone', 'city', 'avatar']

    def validate_password(self, value: str) -> str:
        return make_password(value)



