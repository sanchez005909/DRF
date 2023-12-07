from django.core.management import BaseCommand
import random
from curses.models import Curs, Lesson
from users.models import User
from payments.models import Payment


class Command(BaseCommand):

    def handle(self, *args, **options):

        curses = Curs.objects.all()
        lessons = Lesson.objects.all()
        users = User.objects.all()

        curs_or_lesson = ['curs', 'lesson']
        method_payment = ['cash', 'card']

        payments_list = []
        payments_list_for_create = []

        for _ in range(5):
            random_ = random.choice(curs_or_lesson)
            if random_ == 'curs':
                payments_list.append(
                    {
                        'user': random.choice(users),
                        'curs': random.choice(curses),
                        'sum_payment': 100000,
                        'payment_method': random.choice(method_payment),
                    },
                )
            else:
                payments_list.append(
                    {
                        'user': random.choice(users),
                        'lesson': random.choice(lessons),
                        'sum_payment': 5000,
                        'payment_method': random.choice(method_payment),
                    },
                )

        for payment in payments_list:
            payments_list_for_create.append(Payment(**payment))

        Payment.objects.bulk_create(payments_list_for_create)
