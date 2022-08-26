from django.shortcuts import render
from FamiliarApp.models import Familiar


# Acá podría solicitarle a la BD todos los registros de la tabla Familiar, y enviarlos al html mediante
# la variable contexto, después recorrería con
def familiar(request):
    familiar4 = Familiar(nombre='Federico', parentezco='primo', id=4, fechaCreacion='2022-08-12 17:40:23')
    familiar4.save()
    contexto = {
        'familiar': familiar4
    }
    return render(request, 'familiar.html', contexto)