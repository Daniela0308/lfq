#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TeamSerializer
from ..models.teams import Team

""" #Decorador: convierte una función normal de Django en una API REST
@api_view(['GET'])
def teams_list_api(request):
    teams = Team.objects.all() #obtengo los equipos creados en la db
    serializer = TeamSerializer(teams, many=True) #convierto los datos en json
    return Response(serializer.data) """

class TeamAPI(APIView):
    authentication_classes = []
    permission_classes = []

    #metodo GET para obtener los equipos
    def get(self, request):
        #QuerySet, con la lista de equipos
        teams = Team.objects.all()
        #convertimos los datos en JSON
        serializer = TeamSerializer(teams, many=True)

        return Response(serializer.data)
    
    #metodo POST para crear un equipo
    def post(self, request):
        serializer = TeamSerializer(data=request.data) #Obtiene JSON y lo convierte en objeto django

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
