from rest_framework import serializers
from curses.models import Curs, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CursSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(source='lesson_set.all.count')
    lesson_list = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Curs
        fields = '__all__'

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()
