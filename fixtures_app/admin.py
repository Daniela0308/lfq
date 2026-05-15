from django.contrib import admin
from .models.teams import Team

#decorador para registar el modelo y la clase
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_display = ['name', 'city', 'logo']
    search_fields = ['name']