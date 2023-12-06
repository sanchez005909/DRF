from rest_framework import serializers
from curses.models import Curs, Lesson


class CursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curs
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
