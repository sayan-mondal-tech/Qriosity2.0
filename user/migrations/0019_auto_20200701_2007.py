# Generated by Django 3.0.7 on 2020-07-01 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_auto_20200701_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerdetails',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Player'),
        ),
    ]
