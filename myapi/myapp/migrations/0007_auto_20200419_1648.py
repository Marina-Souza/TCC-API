# Generated by Django 2.0.3 on 2020-04-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20200419_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acionamentos',
            name='idDispositivo',
            field=models.IntegerField(),
        ),
    ]
