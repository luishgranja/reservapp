from django.urls import path , include
from .views import *

app_name = 'recursos'

urlpatterns = [

    path('registrar-recurso', registrar_recurso, name='registrar_recurso'),
    path('consultar', consultar_recursos, name='consultar_recursos'),
    path('editar/<int:id_recurso>', editar_recurso, name='editar_recurso'),

]
