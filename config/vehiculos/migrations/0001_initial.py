# Generated by Django 4.0.5 on 2023-07-21 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(choices=[['Fiat', 'Fiat'], ['Chevrolet', 'Chevrolet'], ['Ford', 'Ford'], ['Toyota', 'Toyota']], max_length=100)),
                ('serie_carroceria', models.CharField(max_length=50)),
                ('serie_motor', models.CharField(max_length=50)),
                ('categoria', models.CharField(choices=[['Particular', 'Particular'], ['Transporte', 'Transporte'], ['Carga', 'Carga']], default='Particular', max_length=50)),
                ('Precio', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('fecha_modificiacion', models.DateTimeField(null=True)),
            ],
        ),
    ]