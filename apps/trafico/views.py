from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView
from apps.trafico.forms import FlujoVehicularForm
from apps.trafico.models import FlujoVehicular, Semaforo, Simulacion

class Inicio(TemplateView):
    template_name = 'index.html'

class VistaSimular(ListView):
    model = Simulacion
    template_name = 'simulacion/inicio_simular.html'
    id_simulacion = None

    def get_queryset(self):
        simulacion = self.model.objects.filter(id = self.id_simulacion)
        return FlujoVehicular.objects.filter(simulacion = simulacion[0].id)    
    
    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['flujos'] = self.get_queryset()
        return contexto
    
    def get(self, request, *args, **kwargs):
        self.id_simulacion = self.crear_simulacion()
        return render(request, self.template_name, self.get_context_data())

    def crear_simulacion(self):
        simulacion = Simulacion.objects.create()

        for s in Semaforo.objects.all():
            FlujoVehicular.objects.create(simulacion=simulacion, semaforo=s)
        
        return simulacion.id

class EditarFlujo(UpdateView):
    pass
    
    
