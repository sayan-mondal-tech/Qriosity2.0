# Generated by Django 3.0.7 on 2020-06-28 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20200628_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='college',
        ),
        migrations.RemoveField(
            model_name='player',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='player',
            name='year',
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=400),
        ),
        migrations.CreateModel(
            name='PlayerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(default='none', max_length=400)),
                ('year', models.CharField(default='1', max_length=10)),
                ('contact', models.IntegerField(blank=True, default=1)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Player')),
            ],
        ),
    ]
