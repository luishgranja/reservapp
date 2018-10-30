from django.db import models
from apps.accounts.models import *
from apps.recursos.models import *
from datetime import date

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    recurso = models.ForeignKey('recursos.Recurso', on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(default=date.today)
    fecha_final = models.DateTimeField(default=date.today)
    observaciones = models.TextField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
