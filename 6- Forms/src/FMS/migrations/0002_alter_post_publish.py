# Generated by Django 4.1.2 on 2022-10-15 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(null=True),
        ),
    ]
