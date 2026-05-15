from django.db import models
from .tournaments import Tournament
from .teams import Team
from .stadiums import Stadium

class Matchday(models.Model):
    #un torneo puede tener varias fechas
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='matchday')
    number = models.PositiveIntegerField()

    def __str__(self):
        return f"Jornada {self.number} - {self.tournament}"

    class Meta:
        ordering = ['number'] #ordenamos por número de fecha

class Match(models.Model):
    #una fecha puede tener varios partidos
    matchday = models.ForeignKey(Matchday, on_delete=models.CASCADE, related_name='matches')
    #muchos partidos pueden tener el mismo equipo de local o visitante
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    #Si borro el estadio ese campo queda como null en el partido que este asignado
    stadium = models.ForeignKey(Stadium, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"