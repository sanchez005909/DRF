from django.contrib.auth.models import AbstractUser
from django.db import models
# from curses.models import NULLABLE
NULLABLE = {'blank': True, 'null': True}
from django.utils.translation import gettext_lazy as _


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):

    username = None
    email = models.CharField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=30, verbose_name='phone', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='city', **NULLABLE)
    avatar = models.ImageField(verbose_name='avatar', **NULLABLE)
    role = models.CharField(max_length=15, choices=UserRoles.choices, default=UserRoles.MEMBER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
