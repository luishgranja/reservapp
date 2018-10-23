from django.db import models
from apps.accounts.models import *
from apps.recursos.models import *
from datetime import date

class Reserva(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_recurso = models.ForeignKey('recursos.Recurso', on_delete=models.CASCADE)
    fecha_inicio = models.DateField(default=date.today)
    fecha_final = models.DateField(default=date.today)
    is_active = models.BooleanField(default=True)
