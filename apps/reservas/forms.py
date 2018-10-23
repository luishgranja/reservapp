from django import forms
from apps.reservas.models import *

class crear_reservas(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('id_recurso', 'fecha_inicio', 'fecha_final', 'is_active')
        labels = {
        'is_active' : 'Activo',
        'id_recurso': 'Recurso a reservar'
        }
