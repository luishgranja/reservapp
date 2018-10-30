from django import forms
from apps.reservas.models import *

class CrearReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('recurso', 'fecha_inicio', 'fecha_final','observaciones' ,'is_active')
        labels = {
        'is_active' : 'Activo',
        'id_recurso': 'Recurso a reservar'
        }

class CrearReservaRecursoForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('fecha_inicio', 'fecha_final','observaciones')
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'class': 'datetimepicker'})
        }


class EditarReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('fecha_inicio', 'fecha_final','observaciones', 'is_active')
        labels = {
        'is_active' : 'Activo'
        }
        help_text = {
        'is_active' : 'Desseleccione esta opción si desea cancelar la reserva del recurso'
        }
