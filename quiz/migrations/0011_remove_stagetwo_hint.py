# Generated by Django 3.0.7 on 2020-07-20 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20200720_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stagetwo',
            name='hint',
        ),
    ]
