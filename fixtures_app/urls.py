from django.urls import path

from .views.teams_views import TeamsListView

urlpatterns = [
    path('equipos/', TeamsListView.as_view(), name='teams_list'),
] 