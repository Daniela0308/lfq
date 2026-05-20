from django.views import generic

from ..models.teams import Team
from ..models.tournaments import Tournament
from ..models.fixtures import Match

class HomeView(generic.TemplateView):
    template_name = 'base/home.html'

    def get_context_data(self):
        return {
        'total_teams': Team.objects.count(),
        'total_tournaments': Tournament.objects.count(),
        'total_matches': Match.objects.count(),
        'active_tournaments': Tournament.objects.count(),
       # 'proximos_partidos': Match.objects.filter(date__isnull=False).order_by('date')[:3],
       # 'resultados_recientes': Match.objects.filter(date__isnull=False).order_by('-date')[:3],
        }