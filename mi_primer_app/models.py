from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    enfermedad = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nombre
    
class Receta(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.TextField(max_length=50)
    elaboracion = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.nombre})"
    