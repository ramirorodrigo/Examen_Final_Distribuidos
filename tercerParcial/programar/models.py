from django.db import models
from administrador.models import Estudiante, Asignatura

class Programacion(models.Model):

    gestion = models.CharField(max_length=7, help_text='                    ')
    grupo = models.IntegerField(help_text='                    ')
    estudiante_id = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura_id = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    def __str__(self):
        return self.gestion

    class Meta:
        ordering = ['-gestion']
