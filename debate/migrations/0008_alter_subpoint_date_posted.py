# Generated by Django 3.2.2 on 2021-05-27 10:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('debate', '0007_alter_argument_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subpoint',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]