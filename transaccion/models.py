from django.db import models
from cuenta.models import Cuenta

class Transaccion(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2);    
    descripcion = models.CharField(max_length=100);
    tipo = models.CharField(max_length=1, choices=(('I', 'Ingreso'), ('E', 'Egreso')));
    created_at = models.DateTimeField(auto_now_add=True);
    updated_at = models.DateTimeField(auto_now=True);
    cuenta_origen = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='cuenta_origen', null=True, blank=True);
    cuenta_destino = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='cuenta_destino', null=True, blank=True);

    class Meta:
        verbose_name = 'Transacción';
        verbose_name_plural = 'Transacciones';
        

    def __str__(self):
        return self.descripcion
