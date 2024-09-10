from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    apellido = models.CharField(max_length=50)
    edad = models.PositiveIntegerField(null=True, blank=True)  
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    altura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True, blank=True)  
    DEPORTE_CHOICES = [
        ('F', 'Futbol'),
        ('R', 'Rugby'),
        ('B', 'Basquet'),
        ('T', 'Tenis'),
        ('A', 'Atletismo'),
    ]
    deporte = models.CharField(max_length=100, choices=DEPORTE_CHOICES, null=True, blank=True)  
    descripcion = models.TextField(null=True, blank=True)  

    def __str__(self):
        return f"{self.nombre}"
