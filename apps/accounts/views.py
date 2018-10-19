from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, update_session_auth_hash
from apps.accounts.forms import *
from django.contrib import messages


@login_required
def signup(request):
    # Usuario que hizo la peticion a la funcion (usuario que esta en la sesion)
    usuario = request.user
    # Validacion para cuando el administrador (is_staff)
    if usuario.is_staff:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Usuario registrado exitosamente')
                form.save()
                return render(request, 'accounts/signup.html', {'form': SignUpForm()})
            else:
                messages.error(request, 'Por favor corrige los errores')
                return render(request, 'accounts/signup.html', {'form': form})
        else:
            form = SignUpForm()
            return render(request, 'accounts/signup.html', {'form': form})
    # En caso de que el usuario no sea admin se redirije al home y se muestra mensaje de error
    else:
        messages.error(request, 'No estas autorizado para realizar esta acción')
        return redirect('accounts:home')


@login_required
def home(request):
    usuario = request.user
    if usuario.is_staff:
        return render(request, 'accounts/home.html', {'user': usuario})
    else:
        return render(request, 'accounts/home.html', {'user': usuario})


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        # Si es un POST se crea el formulario para guardarse
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Has modificado tu perfil exitosamente!')
            return redirect('accounts:home')
        else:
            messages.error(request, 'Por favor corrige los errores')
    # Si es un get se manda un formulario con los datos del usuario
    else:
        form = EditProfileForm(instance=user)
    return render(request, "accounts/edit_profile.html", {'form': form})


@login_required()
def modificar_usuario(request, idUser):
    user = User.objects.get(id=idUser)
    usuario = request.user
    if usuario.is_staff:
        if request.method == 'POST':
            form = EditFullProfile(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Has modificado el usuario ' + user.get_full_name() + ' exitosamente!')
                return redirect('accounts:home')
            else:
                messages.error(request, 'Por favor corrige los errores')
        else:
            form = EditFullProfile(instance=user)
        return render(request, "accounts/edit_user.html", {'form': form})
    else:
        messages.error(request, 'No estas autorizado para realizar esta acción')
        return redirect('accounts:home')


# Listar:
def listar_usuarios():
    usuarios = User.listar_usuarios()
    return usuarios


def consultar_usuarios(request):
    return render(request, 'accounts/listar_usuarios.html', {'usuarios': listar_usuarios})


@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Tu contraseña ha sido cambiada exitosamente')
            return redirect('accounts:home')
        else:
            messages.error(request, 'Por favor corrige los errores')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/edit_pass.html', {'form': form})


@login_required
def cambiar_contrasena_usuario(request, id_user):

    usuario = request.user
    user = User.get_user(id_user)

    if usuario.is_staff:
        if request.method == 'POST':

            form = SetPasswordForm(user, request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, 'Tu contraseña ha sido cambiada exitosamente')
                return redirect('accounts:home')

            else:
                messages.error(request, 'Por favor corrige los errores')

        else:
            form = SetPasswordForm(user)
        return render(request, 'accounts/edit_pass_user.html', {'form': form})
    else:
        messages.error(request, 'No estas autorizado para realizar esta acción')
        return redirect('accounts:home')





