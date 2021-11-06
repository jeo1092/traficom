from django.contrib.auth.forms import AuthenticationForm

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs = {
            'placeholder':'Nombre de Usuario',
        }

        self.fields['password'].widget.attrs = {
            'placeholder':'Contraseña',
        }
       