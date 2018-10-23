from django.shortcuts import render
from .forms import *


def crear_reserva(request):
    usuario = request.user
    form = crear_reservas()
    return render(request, 'reservas/crear_reserva.html', {'form':form})
