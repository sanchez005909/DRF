from django.db import models
NULLABLE = {'blank': True, 'null': True}

# Create your models here.


class Curs(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    image = models.ImageField(verbose_name='картинка', **NULLABLE)
    description = models.TextField(verbose_name='описание')

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
    curs = models.ForeignKey(Curs, verbose_name='курс', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
