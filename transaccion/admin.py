from django.contrib import admin
from transaccion.models import Transaccion

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('monto', 'descripcion', 'tipo', 'cuenta_origen', 'cuenta_destino', 'created_at', 'updated_at');
    
    list_filter = ('tipo', 'created_at', 'updated_at');
    search_fields = ('descripcion', 'cuenta_origen__nombre', 'cuenta_destino__nombre');
    date_hierarchy = 'created_at';
    ordering = ('-created_at',);
