# Generated by Django 2.0.3 on 2020-04-19 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200419_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acionamentos',
            name='idDispositivo',
            field=models.CharField(max_length=20),
        ),
    ]
