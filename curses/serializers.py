from rest_framework import serializers
from curses.models import Curs, Lesson, Subscription
from curses.validators import URLValidator


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ['user', 'course']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'url_video', 'owner']
        validators = [URLValidator(field='url_video')]


class CursSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField(source='lessons.count', default=0)
    subscribers = SubscriptionSerializer(source='subscription_set', many=True, read_only=True)
    lessons_ = LessonSerializer(source='lessons', many=True, read_only=True)

    class Meta:
        model = Curs
        fields = ['id', 'title', 'description', 'owner', 'lessons_count', 'lessons_', 'subscribers']

    def get_lessons_count(self, instance):
        if instance.lessons is None:
            return 0
        return instance.lessons.count()
