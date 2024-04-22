from django.db import models
from user.models import User

class Tipo_cuenta(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tipo de cuenta'
        verbose_name_plural = 'Tipo de cuenta'

    def __str__(self):
        return self.nombre

class Cuenta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    tipo_cuenta = models.ForeignKey(Tipo_cuenta, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuenta'


    def __str__(self):
        return self.nombre