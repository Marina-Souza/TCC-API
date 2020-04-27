# Generated by Django 2.0.3 on 2020-04-17 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acionamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('data', models.DateField()),
            ],
            options={
                'db_table': 'acionamentos',
            },
        ),
        migrations.CreateModel(
            name='Alertas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limiar', models.IntegerField()),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'alertas',
            },
        ),
        migrations.CreateModel(
            name='Coleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idDispositivo', models.IntegerField()),
                ('valor', models.IntegerField()),
                ('data', models.DateField()),
            ],
            options={
                'db_table': 'coleta',
            },
        ),
        migrations.CreateModel(
            name='Dispositivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('GPIOPort', models.IntegerField()),
            ],
            options={
                'db_table': 'dispositivos',
            },
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vazao', models.IntegerField()),
                ('cronIrrigacao', models.BooleanField(default=True)),
                ('umidade', models.IntegerField()),
                ('condutividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Dispositivos')),
            ],
            options={
                'db_table': 'sistema',
            },
        ),
        migrations.AddField(
            model_name='alertas',
            name='idDispositivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Dispositivos'),
        ),
        migrations.AddField(
            model_name='acionamentos',
            name='idDispositivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Dispositivos', verbose_name='Lista de acionamentos realizados'),
        ),
    ]