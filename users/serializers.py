from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'role', 'email', 'phone', 'city', 'avatar', 'is_staff', 'is_superuser']




