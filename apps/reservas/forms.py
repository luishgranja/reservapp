from django import forms
from apps.reservas.models import *
from apps.recursos.models import Recurso

class CrearReservaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CrearReservaForm, self).__init__(*args, *kwargs)
        self.fields['recurso'].queryset = Recurso.objects.filter(estado=True) & Recurso.objects.filter(is_active=True)

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
