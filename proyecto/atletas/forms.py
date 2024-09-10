from django import forms
from django.core.exceptions import ValidationError

from .models import Pais

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()  # Eliminar espacios en blanco

        # Convertir la primera letra a mayúscula
        nombre = nombre.capitalize()

        # Validar que solo contenga letras
        if not nombre.isalpha():
            raise ValidationError('El nombre solo puede contener letras.')

        # Validar longitud del nombre
        if len(nombre) < 3 or len(nombre) > 50:
            raise ValidationError('El nombre debe tener una longitud mínima de 3 letras y máxima de 50.')

        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido', '').strip()  # Eliminar espacios en blanco

        # Convertir la primera letra a mayúscula
        apellido = apellido.capitalize()

        # Validar que solo contenga letras
        if not apellido.isalpha():
            raise ValidationError('El apellido solo puede contener letras.')

        # Validar longitud del apellido
        if len(apellido) < 3 or len(apellido) > 50:
            raise ValidationError('El apellido debe tener una longitud mínima de 3 letras y máxima de 50.')

        return apellido

