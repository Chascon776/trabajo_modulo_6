from django.db import models
from django.utils import timezone
from django import forms

# Create your models here.
PERMISOS = [
    ("visualizar_catalogo", "Puede Visualizar catalogo Vehiculos"),
    ("add_vehiculomodel", "Puede Agregar Vehiculo"), ]


class vehiculos(models.Model):
    options = [
        ["Fiat", "Fiat"], 
        ["Chevrolet", "Chevrolet"],
        ["Ford", "Ford"],
        ["Toyota", "Toyota"]
    ]
    marca = models.CharField(max_length=20, choices = options)
    modelo = models.CharField(max_length=100)
    serie_carroceria = models.CharField(max_length=50)
    serie_motor = models.CharField(max_length=50)
    options = [
        ["Particular", "Particular"], 
        ["Transporte", "Transporte"],
        ["Carga", "Carga"],
        ]
    categoria = models.CharField(max_length=50,choices = options,default='Particular')
    precio = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_modificiacion = models.DateTimeField(null=True)
  
    def __str__(self):
        return self.marca + ' ' + self.modelo
    
    class Meta:
        permissions = PERMISOS