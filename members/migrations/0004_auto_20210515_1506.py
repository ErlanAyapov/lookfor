# Generated by Django 3.1 on 2021-05-15 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='image',
        ),
        migrations.AddField(
            model_name='customer',
            name='picture',
            field=models.CharField(default='0', max_length=2, verbose_name='Сурет'),
        ),
    ]
