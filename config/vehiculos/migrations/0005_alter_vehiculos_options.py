# Generated by Django 4.0.5 on 2023-07-21 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0004_rename_precio_vehiculos_precio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculos',
            options={'permissions': [('add_vehiculomodel', 'Agrega Vehiculo')], 'verbose_name_plural': 'Administrar visualizacion'},
        ),
    ]
