from rest_framework import serializers
from curses.models import Curs, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'owner']


class CursSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField(source='lessons.count')

    class Meta:
        model = Curs
        fields = ['id', 'title', 'description', 'owner', 'lessons_count', 'lessons']

    def get_lessons_count(self, instance):
        return instance.lessons.count()



