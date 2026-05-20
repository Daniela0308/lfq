from django import forms
from ..models.teams import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'city', 'logo']
    
    """ def save(self):
        #creamos el equipo utilizando los datos del formulario
        Team.objects.create(
            name=self.cleaned_data['name'],
            city=self.cleaned_data['city'],
            logo=self.cleaned_data['logo']
        )
         """