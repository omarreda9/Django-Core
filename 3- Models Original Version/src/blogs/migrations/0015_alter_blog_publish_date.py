# Generated by Django 4.1.1 on 2022-09-12 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_alter_blog_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
