# Generated by Django 3.0.7 on 2020-07-16 12:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20200711_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='last_submit',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 16, 18, 3, 49, 562025)),
        ),
    ]
