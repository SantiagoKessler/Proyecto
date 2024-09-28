# En forms.py
from django import forms
from .models import Plan

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['entrenamiento', 'dias', 'horas']  # Asegúrate de incluir todos los campos que deseas
