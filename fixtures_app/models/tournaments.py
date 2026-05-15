from django.db import models
from .teams import Team

class Tournament(models.Model):
    name = models.CharField(max_length=150)
    start_date = models.DateField()
    #relacion muchos a muchos, un torneo puede tener muchos equipos y un equipo puede estar en muchos torneos
    teams = models.ManyToManyField(Team, related_name='tournaments') 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Group(models.Model):
    #Hacemos relacion muchos a uno, varios grupos pueden estar en un torneo y si eliminamos el torneo tambien se eliminan los grupos
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=100)
    #Relacion muchos a muchos: un grupo puede tener muchos equipos y un equipo puede estar en muchos grupos
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return f"Grupo {self.name} del torneo {self.tournament}"