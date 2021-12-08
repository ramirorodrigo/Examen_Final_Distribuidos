from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('calific', views.index, name='calific'),
    path('calificando', views.FormularioCalificacionView.regiscalificar, name='calificando'),
    path('guardarcalific', views.FormularioCalificacionView.procesar_formularioc, name='guardarcalific'),
]