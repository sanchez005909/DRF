from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from curses.models import Curs, Subscription


@shared_task
def send_mail_for_update(pk):
    curs = Curs.objects.get(pk=pk)
    subscriptions = Subscription.objects.filter(course=pk)
    subscribers = []
    for subscription in subscriptions:
        subscribers.append(subscription.user)

    send_mail(
        subject='Update',
        message=f'Обновили курс: {curs.title}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=subscribers
    )
