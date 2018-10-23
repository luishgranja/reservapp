from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    documento = models.CharField(max_length=10, unique = True)
    tipos = ( ('profe', 'Profesor'), ('estudiante', 'Estudiante') )
    tipo =  models.CharField(max_length=10,choices=tipos)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'tipo', 'email','is_active']
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
            user = User.objects.get(id=id_user)
            return user
        except User.DoesNotExist:
            return None

    def get_tipo(self):
        if self.is_staff:
            return 'Administrador'
        if self.tipo == 'profe':
            return 'Profesor'
        if self.tipo == 'estudiante':
            return 'Estudiante'
