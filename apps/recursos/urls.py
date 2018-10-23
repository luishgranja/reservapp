from django.urls import path , include
from .views import *

app_name = 'recursos'

urlpatterns = [

    path('registrar-recurso', registrar_recurso, name='registrar_recurso'),

]
