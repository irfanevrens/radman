# Generated by Django 3.0.5 on 2020-04-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0003_mount'),
    ]

    operations = [
        migrations.AddField(
            model_name='mount',
            name='mount_path',
            field=models.CharField(default='sss', max_length=200),
            preserve_default=False,
        ),
    ]
