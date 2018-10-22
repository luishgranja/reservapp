from django.db import models

class Recurso(models.Model):
    nombre = models.CharField(max_length=20)
    TIPOS = (
        ('Computador','Computador'),
        ('video', 'Video Beam'),
        ('', ''),
        ('', ''),
    )

    tipo = models.CharField(choices=TIPOS, max_length=15, default='Computador')
    is_active = models.BooleanField(default=True)
    ESTADOS = (
        ('Pesimo', 'Pésimo (1)'),
        ('Malo','Malo (2)'),
        ('Regular', 'Regular (3)'),
        ('Bueno', 'Bueno (4)'),
        ('Excelente', 'Excelente (5)'),
    )

    estado = models.CharField(choices=ESTADOS, max_length= 11)
    observaciones = models.CharField(max_length=100)
