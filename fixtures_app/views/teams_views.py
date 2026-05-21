#Renderizar HTML, redireccionar y generar erro si un objeto no existe
#from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
#from django.views import generic
#from django.urls import reverse_lazy

#Imports propios
from ..models.teams import Team
from ..forms.teams_forms import TeamForm


#Lista de equipos
def teams_list(request):
    #QuerySet: colección de objetos de Django
    team = Team.objects.all() #obtenemos todos los equipos que existen
    return render(request, 'teams/teams.html', {'teams_list': team}) 

#Crear equipos
def team_create(request):
    #Si el método de la solicitud es POST, significa que se ha enviado el formulario
    if request.method == 'POST':
        form = TeamForm(request.POST) #Creamos una instancia del formulario con los datos enviados por el usuario
        if form.is_valid(): #Si el formulario es válido, guardamos el nuevo equipo en la base de datos
            form.save()
            return redirect('teams')
    else: #Si el método de la solicitud no es POST, significa que el usuario está accediendo a la página de creación de equipos, por lo que mostramos un formulario vacío
        form = TeamForm()
    #Renderizamos la plantilla 'create_team.html' y pasamos el formulario al contexto para que pueda ser utilizado en la plantilla
    return render(request, 'teams/create_team.html', {'form': form})

#Editar equipos
def team_edit(request, pk):
    #Obtenemos el equipo que se va a editar utilizando su clave primaria (ID). 
    # Si el equipo no existe, se generará un error 404
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        #Creamos una instancia del formulario con los datos enviados por el usuario y el equipo que se va a editar.
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return redirect('teams')
    else:
        form = TeamForm(instance=team)
    #Renderizamos la plantilla 'edit_team.html' y pasamos el formulario y el equipo al contexto para que puedan ser utilizados en la plantilla
    return render(request, 'teams/edit_team.html', {'form': form, 'team': team})

#Eliminar equipos
def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        team.delete()
    
    return redirect('teams')


"""
#Listado de equipos
class TeamsListView(generic.TemplateView):
    template_name = 'teams/teams.html'

    def get_context_data(self):
        teams_list = Team.objects.all()

        return {'teams_list': teams_list}
        
#Creación de equipos
class TeamCreateView(generic.CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'teams/create_team.html'
    success_url = reverse_lazy('teams')

#Editar equipos
class TeamUpdateView(generic.UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'teams/edit_team.html'
    success_url = reverse_lazy('teams')
  
        
     """



