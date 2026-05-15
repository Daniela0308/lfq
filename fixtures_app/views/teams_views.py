#Renderizar HTML, redireccionar y generar erro si un objeto no existe
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
#Imports propios
from ..models.teams import Team

""" #Lista de equipos
def teams_list(request):
    #QuerySet: colección de objetos de Django
    teams = Team.objects.all() #obtenemos todos los equipos que existen
    return render(request, 'teams/teams.html', {'teams': teams}) """

class TeamsListView(generic.TemplateView):
    template_name = 'teams/teams.html'

    """ def get_context_data(self):
        teams_list = Team.objects.all()

        return {'teams_list': teams_list}
         """
    