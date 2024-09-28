from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    apellido = models.CharField(max_length=50)
    edad = models.PositiveIntegerField(null=True, blank=True)  
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    altura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  
    SEXO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    ]
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES, null=True, blank=True)  
    DEPORTE_CHOICES = [
        ('Futbol', 'Futbol'),
        ('Rugby', 'Rugby'),
        ('Basquet', 'Basquet'),
        ('Tenis', 'Tenis'),
        ('Atletismo', 'Atletismo'),
    ]
    deporte = models.CharField(max_length=10, choices=DEPORTE_CHOICES, null=True, blank=True) 
    GRASA_CHOICES = [
        ('6-13%','6-13%'),
        ('14-17%','14-17%'),
        ('18-24%','18-24%'),
        ('25% o mas','25% o mas'),
    ] 
    grasa = models.CharField(max_length=10, choices=GRASA_CHOICES, null=True, blank=True)

    VELOCIDAD_CHOICES = [
        ('4.6 - 4.9 segundos',' 4.6 - 4.9 segundos'),
        ('5.0 - 5.3 segundos','5.0 - 5.3 segundos' ),
        ('5.4 segundos o más', '5.4 segundos o más' ,),
    ]
    velocidad = models.CharField(max_length=20, choices=VELOCIDAD_CHOICES, null=True, blank=True)

    descripcion = models.TextField(null=True, blank=True)  
