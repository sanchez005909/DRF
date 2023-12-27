from datetime import timedelta, datetime

from django.utils import timezone
from celery import shared_task
from users.models import User


@shared_task
def check_last_login():
    users = User.objects.all()

    for user in users:
        now = timezone.now()
        if user.is_active:
            if now - user.last_login > timedelta(days=30):
                user.is_active = False
                user.save()

