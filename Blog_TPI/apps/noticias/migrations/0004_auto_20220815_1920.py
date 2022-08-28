# Generated by Django 3.2 on 2022-08-15 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_auto_20220809_1209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noticia',
            options={'ordering': ('-creado',)},
        ),
        migrations.AddField(
            model_name='noticia',
            name='slug',
            field=models.SlugField(default=0, max_length=250, unique=True, unique_for_date='published'),
            preserve_default=False,
        ),
    ]
