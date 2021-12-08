from django.contrib import admin
from .models import Estudiante, Asignatura

# Register your models here.

admin.site.register([Estudiante, Asignatura])
