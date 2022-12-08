from django import forms
from .models import Viatura

# Create your forms here.
            
class ViaturaForm(forms.ModelForm):
    class Meta:
        model = Viatura
        exclude = ('estado',)
        labels = {
                
                'nome':"Nome",
                'estado_viatura':"Estado",
            }
        widgets = {
                    
                    'nome': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o nome da Viatura",     
                        }
                    ),
                   
                    'estado_viatura': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Informe o estado da Viatura",     
                        } 
                    )
                    
            }
