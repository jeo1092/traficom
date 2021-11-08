from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs = {
            'placeholder':'Nombre de Usuario',
        }

        self.fields['password'].widget.attrs = {
            'placeholder':'Contraseña',
        }

class FormularioRegistro(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs = {
            'placeholder':'Nombre de Usuario',
        }

        self.fields['password1'].widget.attrs = {
            'placeholder':'Contraseña',
        }

        self.fields['password2'].widget.attrs = {
            'placeholder':'Confirmar Contraseña',
        }
