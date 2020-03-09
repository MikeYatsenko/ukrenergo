# Generated by Django 3.0.4 on 2020-03-09 20:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('urlcheck', '0016_auto_20200309_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 9, 20, 8, 30, 456967, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='url',
            name='interval',
            field=models.IntegerField(help_text='Interval in minutes.'),
        ),
        migrations.AlterField(
            model_name='url',
            name='site_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 9, 20, 8, 30, 456990, tzinfo=utc)),
        ),
    ]