# Generated by Django 3.0.7 on 2020-07-20 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20200717_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='last_submit',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 19, 29, 38, 443122)),
        ),
    ]
