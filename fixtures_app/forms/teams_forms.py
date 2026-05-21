from django import forms
from ..models.teams import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'city', 'logo']
        labels = {
            'name': 'Nombre del Equipo',
            'city': 'Ciudad',
            'logo': 'Logo del Equipo',
        } #personalización de etiquetas para los campos del formulario
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Ingrese el nombre del equipo'}),
            'city': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Ingrese la ciudad del equipo'}),
            'logo': forms.FileInput(attrs={'class': 'input'}),
        } #personalización de widgets para los campos del formulario, agregando clases CSS para estilos personalizados.

    def clean_name(self):
        name = self.cleaned_data['name'] #contiene los datos del formulario ya procesados por Django.
        name = name.strip().title() #elimina espacios al inicio y al final del nombre
        
        # Verificamos si existe otro equipo con el mismo nombre, excluyendo el equipo actual (en caso de edición)
        if Team.objects.filter(name__iexact=name).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                'Ya existe un equipo con este nombre.'
                )
        return name
    
    
    """ def save(self):
        #creamos el equipo utilizando los datos del formulario
        Team.objects.create(
            name=self.cleaned_data['name'],
            city=self.cleaned_data['city'],
            logo=self.cleaned_data['logo']
        )
         """