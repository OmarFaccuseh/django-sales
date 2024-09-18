from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Instrumento, Metricas


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class InstrumentoForm(forms.ModelForm):
    class Meta:
        model = Instrumento
        fields = ['name', 'porcentaje_anual', 'congelamiento_dias', 'monto']




'''
class MetricaForm(forms.ModelForm):
    class Meta:
        model = Metricas
        fields = ['total_inversion', 'prom_porcentaje_anual', 'gains_mes', 'gains_anual', 'instrumentos', '']
'''

