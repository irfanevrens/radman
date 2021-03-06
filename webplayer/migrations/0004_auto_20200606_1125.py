# Generated by Django 3.0.5 on 2020-06-06 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0013_mount_active'),
        ('webplayer', '0003_listenerlog_organization'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listenerlog',
            options={'verbose_name': 'Dinleyici kaydı', 'verbose_name_plural': 'Dinleyici kayıtları'},
        ),
        migrations.AlterField(
            model_name='listenerlog',
            name='browser',
            field=models.TextField(blank=True, null=True, verbose_name='Tarayıcı'),
        ),
        migrations.AlterField(
            model_name='listenerlog',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi'),
        ),
        migrations.AlterField(
            model_name='listenerlog',
            name='ip',
            field=models.CharField(max_length=100, verbose_name='IP Adresi'),
        ),
        migrations.AlterField(
            model_name='listenerlog',
            name='mount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stations.Mount', verbose_name='Dinleme Noktası'),
        ),
        migrations.AlterField(
            model_name='listenerlog',
            name='name',
            field=models.TextField(blank=True, null=True, verbose_name='İsim - Soyisim'),
        ),
        migrations.AlterField(
            model_name='listenerlog',
            name='organization',
            field=models.TextField(blank=True, null=True, verbose_name='Grup'),
        ),
        migrations.AlterField(
            model_name='listenerlog',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi'),
        ),
    ]
