from django.urls import path , include
from .views import *

app_name = 'reservas'

urlpatterns = [

    path('crear-reserva', crear_reserva, name='crear_reserva'),
    path('crear/<int:id_recurso>', crear_reserva_recurso, name='crear_reserva_recurso'),
    path('editar-reserva/<int:id_reserva>', editar_reserva, name='editar_reserva'),
    path('consultar', consultar_reservas, name='consultar_reservas'),

]
