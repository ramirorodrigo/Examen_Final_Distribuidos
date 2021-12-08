from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('prog', views.index, name='prog'),
    path('programando', views.FormularioProgramacionView.regisprogramar, name='programando'),
    path('guardarprog', views.FormularioProgramacionView.procesar_formulariop, name='guardarprog'),
]