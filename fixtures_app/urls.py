from django.urls import path

from .views.teams_views import teams_list, team_create, team_edit, team_delete
from .views.home_view import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('equipos/', teams_list, name='teams'),
    path('equipos/crear/', team_create, name='teams_create'),
    path('equipos/editar/<int:pk>/', team_edit, name='teams_edit'),
    path('equipos/eliminar/<int:pk>/', team_delete, name='teams_delete'),
] 
