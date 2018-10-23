from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('recursos/', include('apps.recursos.urls')),
    path('reservas/', include('apps.reservas.urls'))
]
