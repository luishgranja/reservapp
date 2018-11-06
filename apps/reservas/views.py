from django.shortcuts import render, redirect
from apps.reservas.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.recursos.models import Recurso

@login_required
def crear_reserva(request):
    usuario = request.user
    if request.method == 'POST':

        form = CrearReservaForm(request.POST)
        if form.is_valid():
            form_aux = form.save(commit=False)
            form_aux.usuario = usuario
            form_aux.save()
            messages.success(request, 'Reserva generada exitosamente')
            return redirect('accounts:home')
        else:
            messages.error(request, 'Por favor corrige los errores')
            return render(request, 'reservas/crear_reserva.html', {'form': form})
    else:
        form = CrearReservaForm()
        return render(request, 'reservas/crear_reserva.html', {'form':form})

@login_required
def crear_reserva_recurso(request, id_recurso):

    usuario = request.user
    recurso = Recurso.get_recurso(id_recurso)

    if request.method == 'POST':

        form = CrearReservaRecursoForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = usuario

            #Cambiar el estado del recurso para que este ocupado
            recurso.estado = True
            recurso.save()
            reserva.recurso = recurso

            #Guardar el formulario auxiliar con los cambios
            reserva.save()
            form.save_m2m()
            messages.success(request, 'Reserva generada exitosamente')
            return redirect('recursos:consultar_recursos')
        else:
            messages.error(request, 'Por favor corrige los errores')
            return render(request, 'reservas/crear_reserva_recurso.html', {'form': form, 'recurso': recurso.nombre})
    else:
        form = CrearReservaRecursoForm()
        return render(request, 'reservas/crear_reserva_recurso.html', {'form':form, 'recurso': recurso.nombre})

@login_required
def editar_reserva(request, id_reserva):

    usuario = request.user
    reserva = Reserva.objects.get(id=id_reserva)
    recurso = reserva.recurso

    if request.method == 'POST':
        form = EditarReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form_aux = form.save(commit=False)
            form_aux.usuario = usuario
            form_aux.recurso = recurso
            form_aux.save()
            messages.success(request, 'Reserva modificada exitosamente')
            return redirect('reservas:consultar_reservas')
        else:
            messages.error(request, 'Por favor corrige los errores')
            return render(request, 'reservas/editar_reserva.html', {'form': form, 'recurso': recurso.nombre})
    else:
        form = EditarReservaForm(instance=reserva)
        return render (request, 'reservas/editar_reserva.html', {'form': form, 'recurso': recurso.nombre})

@login_required
def consultar_reservas(request):
    usuario = request.user

    if usuario.is_staff:
        reservas = Reserva.objects.all()
    else:
        reservas = Reserva.objects.filter(usuario=usuario)

    return render(request, 'reservas/listar_reservas.html', {'reservas': reservas})
