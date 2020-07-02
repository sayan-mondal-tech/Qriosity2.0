# Generated by Django 3.0.7 on 2020-07-02 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20200625_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staticquestions',
            old_name='answer',
            new_name='answer_x',
        ),
        migrations.RemoveField(
            model_name='staticquestions',
            name='url',
        ),
        migrations.AddField(
            model_name='staticquestions',
            name='answer_y',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='staticquestions',
            name='answer_z',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='staticquestions',
            name='level',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
