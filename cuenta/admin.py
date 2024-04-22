from django.contrib import admin
from cuenta.models import Cuenta
from cuenta.models import Tipo_cuenta

@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('nombre','usuario', 'saldo', 'create_at', 'update_at')

@admin.register(Tipo_cuenta)
class Tipo_cuentaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'create_at', 'update_at')