from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .forms import FormularioProgramacion
from .models import Programacion
# Create your views here.


def index(request):
    return render(request, 'baseprog.html')



class FormularioProgramacionView(HttpRequest):
    def regisprogramar(request, *args, **kwargs):
        programar = FormularioProgramacion()
        return render(request, 'prog/formprog.html', {"form":programar})
    def procesar_formulariop(request):
        programar = FormularioProgramacion(request.POST)
        if programar.is_valid():
            programar.save()
        programar = FormularioProgramacion()
        return render(request, 'prog/formprog.html', {"form":programar, "mensaje": 'ok'})

