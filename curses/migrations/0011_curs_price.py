# Generated by Django 5.0 on 2023-12-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curses', '0010_remove_curs_lessons_curs_lessons'),
    ]

    operations = [
        migrations.AddField(
            model_name='curs',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]