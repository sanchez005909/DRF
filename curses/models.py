from django.conf import settings
from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Curs(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    image = models.ImageField(verbose_name='картинка', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    lessons = models.ForeignKey('Lesson', on_delete=models.CASCADE, **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)
    price = models.PositiveIntegerField(default=1)
    is_paid = models.BooleanField(default=False, name="is_paid")
    # user = models.ForeignKey(User.email, on_delete=models.CASCADE, **NULLABLE, name='')

    @property
    def display_price(self) -> str:
        return '${0:.2f}'.format(self.price / 100)

    @property
    def stripe_price_data(self) -> dict:
        return {
            'currency': 'usd',
            'unit_amount': self.price,
            'product_data': {
                'name': self.title,
            },
        }

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(verbose_name='Картинка', **NULLABLE)
    url_video = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(Curs, on_delete=models.CASCADE, **NULLABLE, verbose_name='курс')

