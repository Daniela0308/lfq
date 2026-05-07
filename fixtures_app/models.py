# fixtures_app/models.py

from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, blank=True)
    logo   = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Equipos'


class Torneo(models.Model):
    nombre     = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    equipos    = models.ManyToManyField(Equipo, related_name='torneos')
    creado_en  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Jornada(models.Model):
    torneo  = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name='jornadas')
    numero  = models.PositiveIntegerField()

    def __str__(self):
        return f"Jornada {self.numero} - {self.torneo}"

    class Meta:
        ordering = ['numero']


class Partido(models.Model):
    jornada     = models.ForeignKey(Jornada, on_delete=models.CASCADE, related_name='partidos')
    equipo_local    = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_local')
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_visitante')
    fecha       = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante}"