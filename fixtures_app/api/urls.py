from django.urls import path

from .api_views import TeamAPI

urlpatterns = [
    path('equipos/', TeamAPI.as_view() , name='teams_api')
] 