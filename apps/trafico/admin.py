from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import EstadoSemaforo, FlujoVehicular, Semaforo, Simulacion

class SemaforoResource(resources.ModelResource):
    class Meta:
        model = Semaforo

class SemaforoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['latitud']
    list_display = ('id','latitud','longitud')
    resource_class = SemaforoResource

class FlujoVehicularResource(resources.ModelResource):
    class Meta:
        model = FlujoVehicular

class FlujoVehicularAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['simulacion__id']
    list_display = ('descripcion','simulacion','semaforo', 'imagen_captada')
    resource_class = SemaforoResource

admin.site.register(Semaforo, SemaforoAdmin)
admin.site.register(FlujoVehicular, FlujoVehicularAdmin)
admin.site.register(Simulacion)
admin.site.register(EstadoSemaforo)
