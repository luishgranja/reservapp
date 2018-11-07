from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def registrar_recurso(request):
    usuario = request.user
    if usuario.is_staff:
        if request.method == 'POST':
            form = registro_recurso(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Recurso registrado exitosamente')
                return render(request, 'recursos/registro_recurso.html', {'form': registro_recurso()})
            else:
                messages.error(request, 'Por favor corrige los errores')
                return render(request, 'recursos/registro_recurso.html', {'form':form})
        else:
            form = registro_recurso()
            return render(request, 'recursos/registro_recurso.html', {'form':form})
    else:
        messages.error(request, 'No estas autorizado para realizar esta acción')
        return redirect('accounts:home')

# Listar recursos
def listar_recursos():
    recursos = Recurso.listar_recursos()
    return recursos

def consultar_recursos(request):
    return render(request, 'recursos/listar_recursos.html', {'recursos': listar_recursos})


#Editar recurso
@login_required
def editar_recurso(request, id_recurso):
    recurso = Recurso.get_recurso(id_recurso)
    usuario = request.user
    if usuario.is_staff:
        if request.method == 'POST':
            form = registro_recurso(request.POST, instance=recurso)
            if form.is_valid():
                form.save()
                messages.success(request, 'Recurso modificado exitosamente')
                return redirect('recursos:consultar_recursos')
            else:
                messages.error(request, 'Por favor corrige los errores')
                return render(request, 'recursos/editar_recurso.html', {'form':form})
        else:
            form = registro_recurso(instance=recurso)
            return render(request, 'recursos/editar_recurso.html', {'form':form})
    else:
        messages.error(request, 'No estas autorizado para realizar esta acción')
        return redirect('accounts:home')
