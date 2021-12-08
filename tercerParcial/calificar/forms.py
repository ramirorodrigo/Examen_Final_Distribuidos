from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.db.models.base import Model
from django.forms import fields, widgets

from .models import Calificacion


class FormularioCalificacion(forms.ModelForm):
    #email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address.")
    class Meta:
        model = Calificacion
        fields = '__all__'
        #widgets = {'fecha': forms.EmailField}
