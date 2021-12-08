from django.db import models
from administrador.models import Estudiante, Asignatura

class Calificacion(models.Model):
    parcial_1 = models.IntegerField(default=0, help_text='                    ')
    parcial_2 = models.IntegerField(default=0, help_text='                    ')
    parcial_3 = models.IntegerField(default=0, help_text='                    ')
    practica = models.IntegerField(default=0, help_text='                    ')
    laboratorio = models.IntegerField(default=0, help_text='                    ')
    ex_final = models.IntegerField(default=0, help_text='                    ')
    estudiante_id = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura_id = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.estudiante_id)

    class Meta:
        ordering = ['-estudiante_id']

