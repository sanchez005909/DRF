# Generated by Django 5.0 on 2023-12-23 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curses', '0012_curs_оплачено_'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curs',
            old_name='Оплачено?',
            new_name='is_paid',
        ),
        migrations.AlterField(
            model_name='curs',
            name='price',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
