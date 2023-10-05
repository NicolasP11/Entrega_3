from django.db import models

# Create your models here.

class Comida(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=120)
    precio = models.IntegerField()

class Bebida(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()

class Postre(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()