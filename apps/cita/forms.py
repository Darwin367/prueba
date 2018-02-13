from django import forms

from apps.cita.models import Citas


class CitaForm(forms.ModelForm):

    class Meta:
        model=Citas

        fields=[
            'nombre',
            'fecha_nacimiento',
            'telefono',
            'tipo_cita',
            'dia',
            'inicio_cita',
            'finaliza_cita',
            
        ]
        labels={
            'Nombre':'nombre',
            'Fecha de nacimiento':'fecha_nacimiento',
            'Telefono':'telefono',
            'Tipo de cita':'tipo_cita',
            'Dia ':'dia',
            'Inicio de cita':'inicio_cita',
            'Finalizacion de cita':'finaliza_cita',
            

        }
        widgets={

            'nombre':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control', 'placeholder':' Año-Mes-Día'}),
            'telefono': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefono'}),
            'tipo_cita': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tipo de cita'}),
            'dia': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fecha Año-Mes-Día'}),
            'inicio_cita': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hora militar'}),
            'finaliza_cita': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hora militar'}),
            

        }
