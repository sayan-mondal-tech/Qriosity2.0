# Generated by Django 3.0.7 on 2020-07-04 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20200704_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage_2',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
