# Generated by Django 3.0.5 on 2020-04-30 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0006_remove_mount_mount_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='mount',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]