# Generated by Django 4.0.5 on 2023-07-21 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculos',
            name='Precio',
            field=models.PositiveIntegerField(),
        ),
    ]