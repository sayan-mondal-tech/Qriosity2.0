# Generated by Django 3.0.7 on 2020-06-18 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_remove_staticquestions_intans'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audioquestions',
            name='intans',
        ),
    ]
