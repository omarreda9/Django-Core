# Generated by Django 4.1.1 on 2022-09-12 15:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0012_blog_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
