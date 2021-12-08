from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .forms import FormularioCalificacion
from .models import Calificacion
# Create your views here.


def index(request):
    return render(request, 'basecalific.html')



class FormularioCalificacionView(HttpRequest):
    def regiscalificar(request, *args, **kwargs):
        calificar = FormularioCalificacion()
        return render(request, 'calific/formcalific.html', {"form":calificar})
    def procesar_formularioc(request):
        calificar = FormularioCalificacion(request.POST)
        if calificar.is_valid():
            calificar.save()
        calificar = FormularioCalificacion()
        return render(request, 'calific/formcalific.html', {"form":calificar, "mensaje": 'ok'})

