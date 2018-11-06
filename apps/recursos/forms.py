from django import forms
from apps.recursos.models import *

class registro_recurso(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ('nombre', 'tipo', 'condicion', 'observaciones', 'is_active')
        labels = {
        'is_active': 'Activo',
        }
