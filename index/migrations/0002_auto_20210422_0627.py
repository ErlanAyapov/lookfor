# Generated by Django 3.1 on 2021-04-22 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='jus',
            field=models.CharField(blank=True, default='Білмеймін', max_length=90, verbose_name='Жүз'),
        ),
        migrations.AddField(
            model_name='article',
            name='ru',
            field=models.CharField(blank=True, default='Білмеймін', max_length=90, verbose_name='Ру'),
        ),
    ]
