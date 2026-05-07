from django.contrib import admin
from .models import Equipo, Torneo, Jornada, Partido

admin.site.register(Equipo)
admin.site.register(Torneo)
admin.site.register(Jornada)
admin.site.register(Partido)