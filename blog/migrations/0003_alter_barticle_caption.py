# Generated by Django 3.2.2 on 2021-05-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210525_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barticle',
            name='caption',
            field=models.CharField(default='Wanna read more?', max_length=100),
        ),
    ]