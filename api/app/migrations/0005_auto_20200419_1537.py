# Generated by Django 2.0.3 on 2020-04-19 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200419_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acionamentos',
            name='idDispositivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Dispositivos'),
        ),
    ]
