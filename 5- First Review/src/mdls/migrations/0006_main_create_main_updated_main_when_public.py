# Generated by Django 4.1.1 on 2022-10-05 18:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mdls', '0005_main_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='main',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='main',
            name='when_public',
            field=models.DateTimeField(null=True),
        ),
    ]
