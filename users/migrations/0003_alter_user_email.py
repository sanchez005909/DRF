# Generated by Django 5.0 on 2023-12-07 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_username_user_avatar_user_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(unique=True, verbose_name='email'),
        ),
    ]