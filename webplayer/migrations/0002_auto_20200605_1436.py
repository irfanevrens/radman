# Generated by Django 3.0.5 on 2020-06-05 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0012_auto_20200605_1434'),
        ('webplayer', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Log',
            new_name='ListenerLog',
        ),
    ]
