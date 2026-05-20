from django.urls import path

from .views.teams_views import TeamsListView, TeamCreateView
from .views.home_view import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('equipos/', TeamsListView.as_view(), name='teams'),
    path('equipos/crear/', TeamCreateView.as_view(), name='teams_create'),
] 
