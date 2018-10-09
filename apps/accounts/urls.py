from django.urls import path , include
from apps.accounts.views import *
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    path('registro/', signup, name='registro'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='accounts/login.html'),name='login'),
    path('dashboard/', home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('editar/perfil/', edit_profile, name='edit_profile'),
    path('editar/perfil/user/<int:idUser>', modificar_usuario, name = 'modificar_usuario'),
    path('consultar/usuarios/' , consultar_usuarios, name = 'consultar'),

]