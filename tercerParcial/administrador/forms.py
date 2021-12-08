from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.db.models.base import Model
from django.forms import fields, widgets

from .models import Estudiante, Asignatura


class FormularioEstudiante(forms.ModelForm):
    #email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address.")
    class Meta:
        model = Estudiante
        fields = ('nombre', 'paterno', 'materno', 'ru', 'email', 'ci')
        #widgets = {'fecha': forms.EmailField}

class FormularioAsignatura(forms.ModelForm):
    #email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address.")
    class Meta:
        model = Asignatura
        fields = '__all__'
        #widgets = {'fecha': forms.EmailField}
