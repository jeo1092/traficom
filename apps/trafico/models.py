from django.db import models
from django.db.models.deletion import CASCADE
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
    id = models.AutoField(primary_key=True)
    semaforo = models.ForeignKey(Semaforo, on_delete=models.CASCADE)

class FlujoVehicular(models.Model):
    id = models.AutoField(primary_key=True)
    
    class DescFlujoVehicular(models.TextChoices):
        NULO = 'FN', _('Nulo')
        BAJO = 'FB', _('Bajo')
        MEDIO = 'FM', _('Medio')
        ALTO = 'FA', _('Alto')

    descripcion = models.CharField(max_length=2, choices=DescFlujoVehicular.choices, default=DescFlujoVehicular.NULO)
    imagen_captada = models.URLField('URL_Imagen', null=True)
    simulacion = models.ForeignKey(Simulacion, on_delete=models.CASCADE, null = True)
    semaforo = models.ForeignKey(Semaforo, on_delete = models.DO_NOTHING, null = True)


