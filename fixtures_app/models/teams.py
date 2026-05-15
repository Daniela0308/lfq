from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    city = models.CharField(max_length=100, blank=True, verbose_name='Ciudad')
    logo = models.ImageField(upload_to='teams/', blank=True, null=True, verbose_name='Logo')

    def __str__(self):
        return self.name

    #Configuracion del modelo
    class Meta:
        ordering = ['name'] #ordenamos las consultas alfabéticamente por name
        verbose_name_plural = 'Equipos' #para mostrar en el admin