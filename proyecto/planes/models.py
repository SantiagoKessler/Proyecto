from django.db import models

class Plan(models.Model):
    ENTRENAMIENTO_CHOICES = [
        ('fuerza', 'fuerza'),
        ('resistencia', 'resistencia'),
        ('velocidad', 'velocidad'),
        ('potencia', 'potencia')
    ]
    entrenamiento = models.CharField(max_length=20, choices=ENTRENAMIENTO_CHOICES, null=False, blank=False)  
    
    DIAS_CHOICES = [
        ('1 a 3 dias', '1 a 3 dias'),
        ('3 a 5 dias', '3 a 5 dias'),
        ('5 a 7 dias', '5 a 7 dias')
    ]
    dias = models.CharField(max_length=20, choices=DIAS_CHOICES, null=False, blank=False)  

    HORAS_CHOICES = [
        ('menos de una hora', 'menos de una hora'),
        ('una a dos horas', 'una a dos horas'),
        ('mas de dos horas', 'mas de dos horas'),
    ]
    horas = models.CharField(max_length=30, choices=HORAS_CHOICES, null=False, blank=False)  
 