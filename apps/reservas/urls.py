from django.urls import path , include
from .views import *

app_name = 'reservas'

urlpatterns = [

    path('crear-reserva', crear_reserva, name='crear_reserva'),

]
