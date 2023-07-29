from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    kilometraje = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.marca}, {self.modelo} - {self.anio}- {self.kilometraje}km"

class Moto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    kilometraje = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.marca}, {self.modelo} - {self.anio}, {self.kilometraje}km"

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre} - {self.email} - tel: {self.telefono}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre} - {self.email} - tel: {self.telefono}"
