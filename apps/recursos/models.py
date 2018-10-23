from django.db import models
from apps.accounts.models import *
from apps.reservas.models import *

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
    observaciones = models.TextField(max_length=150)
    usuarios = models.ManyToManyField(User, through = Reserva)

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
