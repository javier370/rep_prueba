from django.urls import path
from cuenta.views import prueba, get_cuentas

urlpatterns = [
    path('cuenta/prueba', prueba),
    path('cuenta/get-cuentas', get_cuentas),
]