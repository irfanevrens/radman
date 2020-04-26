# Generated by Django 3.0.5 on 2020-04-26 07:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0002_station_port'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('mount_id', models.IntegerField()),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stations.Station')),
            ],
        ),
    ]
