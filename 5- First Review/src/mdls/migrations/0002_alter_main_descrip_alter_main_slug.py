# Generated by Django 4.1.1 on 2022-10-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='descrip',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
