from users.models import User

from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@ad.ad',
            first_name='san',
            last_name='dsa',
            is_active=True,
            is_staff=True,
            is_superuser=False,
        )

        user.set_password("12345")
        user.save()