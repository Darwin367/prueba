from django import forms

from apps.paciente.models import Pacientes


class PacienteForm(forms.ModelForm):

    class Meta:
        model=Pacientes

        fields=[
            'nombre',
            'fecha_nacimiento',
            'telefono',
            'nota',
            
            
        ]
        labels={
            'Nombre':'nombre',
            'Fecha nacimiento':'fecha_nacimiento',
            'Telefono':'telefono',
            'Nota':'nota',
            

        }
        widgets={

            'nombre':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Año-Mes-Día'}),
            'telefono': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefono'}),
            'nota': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nota'}),
           
            

        }
