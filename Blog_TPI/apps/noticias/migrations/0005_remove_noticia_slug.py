# Generated by Django 3.2 on 2022-08-15 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_auto_20220815_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='slug',
        ),
    ]
