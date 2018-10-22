from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def registrar_recurso(request):
    usuario = request.user

    if request.method == 'POST':
        form = registro_recurso(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recurso registrado exitosamente')
            return render(request, 'recursos/registro_recurso.html', {'form': registro_recurso()})
        else:
            messages.success(request, 'Por favor corrige los errores')
            return render(request, 'recursos/registro_recurso.html', {'form':form})
    else:
        form = registro_recurso()
        return render(request, 'recursos/registro_recurso.html', {'form':form})
