from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .forms import FormularioEstudiante, FormularioAsignatura
from .models import Estudiante
# Create your views here.

def lista(request):
    datos = {
        'estudiantes': Estudiante.objects.all(),
    }
    return render(request, 'admins/lista.html', datos)

def index(request):
    return render(request, 'admins/index.html')

def indeex(request):
    return render(request, 'indeex.html')

def tests(request):
    return render(request, 'base.html')


class FormularioEstudiantesView(HttpRequest):
    def regisestudiante(request, *args, **kwargs):
        estudiante = FormularioEstudiante()
        return render(request, 'admins/formest.html', {"form":estudiante})
    def procesar_formulario(request):
        estudiante = FormularioEstudiante(request.POST)
        if estudiante.is_valid():
            estudiante.save()
            estudiante = FormularioEstudiante()
        return render(request, 'admins/formest.html', {"form":estudiante, "mensaje": 'ok'})

class FormularioAsignaturaView(HttpRequest):
    def regisasignatura(request, *args, **kwargs):
        asignatura = FormularioAsignatura()
        return render(request, 'admins/formasig.html', {"form":asignatura})
    def procesar_formularioa(request):
        asignatura = FormularioAsignatura(request.POST)
        if asignatura.is_valid():
            asignatura.save()
            asignatura = FormularioAsignatura()
        return render(request, 'admins/formasig.html', {"form":asignatura, "mensaje": 'ok'})
