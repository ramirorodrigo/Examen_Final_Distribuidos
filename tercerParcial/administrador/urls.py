from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('listar', views.lista, name='lista'),
    path('index', views.index, name='index'),
    path('', views.indeex, name='indeex'),
    path('test', views.tests, name='test'),
    path('RegistrarEstudiante', views.FormularioEstudiantesView.regisestudiante, name='RegistrarEstudiante'),
    path('guardarEstudiante', views.FormularioEstudiantesView.procesar_formulario, name='guardarEstudiante'), 
    path('RegistrarAsignatura', views.FormularioAsignaturaView.regisasignatura, name='RegistrarAsignatura'),
    path('guardarAsignatura', views.FormularioAsignaturaView.procesar_formularioa, name='guardarAsignatura'),
]