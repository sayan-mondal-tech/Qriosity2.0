# Generated by Django 3.0.7 on 2020-07-02 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20200702_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage1',
            name='level',
            field=models.IntegerField(blank=True),
        ),
    ]
