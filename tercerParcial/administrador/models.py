from django.db import models
from django.db.models.base import Model

class Estudiante(models.Model):
    nombre = models.CharField(max_length=20, help_text='                  ')
    paterno = models.CharField(max_length=15, help_text='                  ')
    materno = models.CharField(max_length=15, help_text='                  ')
    ru = models.CharField(max_length=10, unique=True, help_text='                  ')
    email = models.EmailField(max_length=190, unique=True, help_text='                  ' )
    ci = models.CharField(max_length=12, unique=True, help_text='                  ')

    def __str__(self):
        return self.nombre + ' ' + self.paterno + ' ' + self.materno

    class Meta:
        ordering = ['-paterno', 'materno', 'nombre']

class Asignatura(models.Model):
    nombre = models.CharField(max_length=30, help_text='                  ')
    sigla = models.CharField(max_length=6, unique=True, help_text='                  ')
    horas = models.IntegerField(null=True, blank=True)
    semestre = models.IntegerField(help_text='                  ')

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['-nombre']