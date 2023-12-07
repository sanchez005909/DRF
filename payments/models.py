from django.db import models
from django.utils import timezone

from curses.models import Curs, Lesson, NULLABLE
from users.models import User


# Create your models here.
class Payment(models.Model):
    CASH_PAYMENT = 'cash'
    СARD_PAYMENT = 'card'

    PAYMENT = (
        (CASH_PAYMENT, 'Оплата наличными'),
        (СARD_PAYMENT, 'Оплата картой'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='оплата')

    date_payment = models.DateField(default=timezone.now, verbose_name='дата оплаты')
    curs = models.ForeignKey(Curs, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='урок', **NULLABLE)

    sum_payment = models.IntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=20, choices=PAYMENT, verbose_name='способ оплаты')

    def __str__(self):
        return f'Плательщик: {self.user}\nСумма оплаты: {self.sum_payment}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
