from django.db import models
from django.utils.translation import gettext_lazy as _

class Simulacion(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = 'Simulacion'
        verbose_name_plural = 'Simulaciones'
    
    def __str__(self):
        return str(self.id)

class Semaforo(models.Model):
    id = models.AutoField(primary_key=True)
    latitud = models.FloatField('Latitud')
    longitud = models.FloatField('Longitud')

    def __str__(self):
        return str(self.id)

class EstadoSemaforo(models.Model):
    semaforo = models.ForeignKey(Semaforo, on_delete=models.CASCADE)
    simulacion = models.ForeignKey(Simulacion, on_delete=models.CASCADE, null=True)

class FlujoVehicular(models.Model):
    id = models.AutoField(primary_key=True)
    
    class DescFlujoVehicular(models.TextChoices):
        NULO = 'Nulo', _('Nulo')
        BAJO = 'Bajo', _('Bajo')
        MEDIO = 'Medio', _('Medio')
        ALTO = 'Alto', _('Alto')

    descripcion = models.CharField(max_length=5, choices=DescFlujoVehicular.choices, default=DescFlujoVehicular.NULO)
    imagen_captada = models.URLField('URL_Imagen', null=True)
    simulacion = models.ForeignKey(Simulacion, on_delete=models.CASCADE, null = True)
    semaforo = models.ForeignKey(Semaforo, on_delete = models.DO_NOTHING, null = True)


