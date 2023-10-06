from django.db import models

# Create your models here.

class Comida(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.precio}"

class Bebida(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} - {self.precio}"

class Postre(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.precio}"