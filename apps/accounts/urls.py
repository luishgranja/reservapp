from django.urls import path , include
from apps.accounts.views import *
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    path('registrar-usuarios', signup, name='registro'),
    path('', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='accounts/login.html'),name='login'),
    path('dashboard', home, name='home'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('editar-perfil', edit_profile, name='edit_profile'),
    path('editar-password', cambiar_contrasena, name='cambiar_contrasena'),
    path('editar-password/usuario/<int:id_user>', cambiar_contrasena_usuario, name='cambiar_contrasena_usuario'),
    path('editar-perfil/usuario/<int:idUser>', modificar_usuario, name = 'modificar_usuario'),
    path('consultar-usuarios', consultar_usuarios, name = 'consultar'),

]
