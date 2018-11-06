from django.db import models
from apps.accounts.models import *
from apps.reservas.models import *

class Recurso(models.Model):
    nombre = models.CharField(max_length=30)
    TIPOS = (
        ('Computador','Computador de Mesa'),
        ('video', 'Video Beam'),
        ('Bafle', 'Bafle'),
        ('Portatil', 'Portatil'),
        ('cable-vga', 'Cable VGA'),
        ('cable-poder', 'Cable poder'),
        ('cable-hdmi', 'Cable HDMI'),
    )

    tipo = models.CharField(choices=TIPOS, max_length=15, default='Computador')
    is_active = models.BooleanField(default=True)
    CONDICIONES = (
        ('Pesimo', 'Pésimo (1)'),
        ('Malo','Malo (2)'),
        ('Regular', 'Regular (3)'),
        ('Bueno', 'Bueno (4)'),
        ('Excelente', 'Excelente (5)'),
    )

    condicion = models.CharField(choices=CONDICIONES, max_length= 11, default='Excelente')
    observaciones = models.TextField(max_length=150)
    usuarios = models.ManyToManyField(User, through = Reserva)
    estado = models.BooleanField(default=False)


    def __str__(self):
        return self.nombre

    @staticmethod
    def listar_recursos():
        try:
            recursos = Recurso.objects.all()
            return recursos
        except Recurso.DoesNotExist:
            return None

    def get_recurso(id_recurso):
        try:
            recurso = Recurso.objects.get(id=id_recurso)
            return recurso
        except Recurso.DoesNotExist:
            return None
