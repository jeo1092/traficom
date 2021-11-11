from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, View
from apps.trafico.models import EstadoSemaforo, FlujoVehicular, Semaforo, Simulacion

class Inicio(TemplateView):
    template_name = 'index.html'

class VistaSimular(ListView):
    model = Simulacion
    template_name = 'simulacion/inicio_simular.html'
    id_simulacion = None

    def get_queryset(self):
        simulacion = self.model.objects.get(id = self.id_simulacion)
        return FlujoVehicular.objects.filter(simulacion = simulacion.id)    
    
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

class EditarFlujo(View):
    model = FlujoVehicular
    template_name = 'simulacion/editar_flujo.html'
    id_flujo = None
    desc_flujo = None

    def get_queryset(self):
        flujo = self.model.objects.get(id = self.id_flujo)
        return flujo   
    
    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['flujo'] = self.get_queryset()
        return contexto
    
    def get(self, request, pk, desc, *args, **kwargs):
        self.id_flujo = pk
        self.desc_flujo = desc
        self.actualizar_desc_flujo()
        return render(request, self.template_name, self.get_context_data())

    def actualizar_desc_flujo(self):
        flujo = self.model.objects.get(id = self.id_flujo)
        flujo.descripcion = self.desc_flujo
        flujo.save()

class ActualizarFlujo(UpdateView):
    model = FlujoVehicular
    template_name = 'simulacion/inicio_simular.html'
    id_simulacion = None
    
    def get_queryset(self):
        simulacion = Simulacion.objects.get(id = self.id_simulacion)
        return self.model.objects.filter(simulacion = simulacion.id)    
    
    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['flujos'] = self.get_queryset()
        return contexto
    
    def post(self, request, pk, *args, **kwargs):
        flujo = self.model.objects.get(id = pk)
        flujo.imagen_captada = request.POST.get("imagen_captada", None)
        self.id_simulacion = flujo.simulacion.id
        flujo.save()
        return render(request, self.template_name, self.get_context_data())

class Simular(ListView):
    template_name = 'simulacion/inicio_simular.html'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def obtener_estados(self):
        pass

        
    
    
