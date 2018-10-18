from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    documento = models.CharField(max_length=10, unique = True)
    tipos = ( ('profe', 'Profesor'), ('estudiante', 'Estudiante') )
    tipo =  models.CharField(max_length=10,choices=tipos)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'tipo', 'email' , 'username' ,'is_active']
    USERNAME_FIELD = 'documento'

    @staticmethod
    def listar_usuarios():
        try:
            usuarios = User.objects.all()
            return usuarios
        except User.DoesNotExist:
            return None

    def get_user(id_user):
        try:
            user = User.objects.filter(id=id_user).first()
            return user
        except User.DoesNotExist:
            return None