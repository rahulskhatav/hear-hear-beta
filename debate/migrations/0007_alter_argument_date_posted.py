# Generated by Django 3.2.2 on 2021-05-24 12:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('debate', '0006_alter_motion_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='argument',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
