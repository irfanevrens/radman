# Generated by Django 3.0.5 on 2020-05-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0009_mount_mount_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='mount',
            name='slug',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
    ]
