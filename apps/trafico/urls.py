from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.trafico.views import *

urlpatterns = [
    path('vista_simulacion/', login_required(VistaSimular.as_view()), name='vista_simulacion'),
    path('editar_flujo/<int:pk>/', login_required(EditarFlujo().as_view()), name='editar_flujo'),
]
