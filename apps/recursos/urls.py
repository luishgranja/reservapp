from django.urls import path , include
from .views import *

urlpatterns = [

    path('registro/', registrar_recurso, name='registrar_recurso'),

]