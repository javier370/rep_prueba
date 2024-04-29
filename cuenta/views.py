from django.shortcuts import render
from cuenta.models import Cuenta

def get_cuentas(request):
    cuentas = Cuenta.objects.all() # select * from cuenta
    
    return render(request, 'cuentas.html', {
        'cuentas': cuentas
        
        })


# ruta: /cuenta/prueba

def prueba(request):
    msn = 'Hola Mundo desde cuenta'
    return render(request, 'prueba.html', 
                  {
                      'msn' : msn,
                  })
