from django.contrib.auth.models import AbstractUser
from django.db import models
from curses.models import NULLABLE


# Create your models here.
class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=30, verbose_name='phone', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='city', **NULLABLE)
    avatar = models.ImageField(verbose_name='avatar', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
