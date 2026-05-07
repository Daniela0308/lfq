from django.urls import path
from . import views

urlpatterns = [
    path('',                              views.lista_equipos,  name='lista_equipos'),
    path('torneo/nuevo/',                 views.crear_torneo,   name='crear_torneo'),
    #path('torneo/<int:torneo_id>/',       views.ver_fixture,    name='ver_fixture'),
    #path('torneo/<int:torneo_id>/pdf/',   views.exportar_pdf,   name='exportar_pdf'),
    #path('torneo/<int:torneo_id>/excel/', views.exportar_excel, name='exportar_excel'),
] 