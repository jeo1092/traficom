from django import forms
from django.forms import widgets
from .models import FlujoVehicular

class FlujoVehicularForm(forms.ModelForm):
    class Meta:
        model = FlujoVehicular
        fields = ['semaforo', 'descripcion', 'imagen_captada']
        labels = {
            'semaforo':'ID Semaforo',
            'descripcion': 'Descripcion',
            'imagen_captada': 'URL Imagen',
        }
        widgets = {
            'semaforo': forms.TextInput(
                attrs={
                    'type':'text',
                    'readonly':'readonly',
                }
            )
        }