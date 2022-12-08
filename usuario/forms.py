from django import forms
from .models import Funcionario, Instrutor, Aluno, Mecanico

# Create your forms here.
            
class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        exclude = ('estado',)
        labels = {
                
                'primeiro_nome':"Primeiro Nome",
                'sobrenome':"Sobrenome",
                'bi':"Bilhete de Identidade",
                'nacionalidade':"Nacionalidade",
                'contacto':"Contacto",
                'sexo':"Sexo",
                'endereco':"Endereço",
                'nivel_academico':"Nivel Academico",
                'profissao': "Profissão",
            }
        widgets = {
                    
                    'primeiro_nome': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o seu nome",     
                        }
                    ),
                    'sobrenome': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o seu sobrenome",     
                        }
                    ),
                    'bilhete': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o seu Bilhete de Identidade",     
                        }
                    ),
                    'nacionalidade': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe a sua nacionalidade",     
                        }
                    ),

                    'contacto': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o seu endereço",     
                        }
                    ),
                   
                    'sexo': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Informe o genero",     
                        } 
                    ),

                    'nivel_academico': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Informe o seu nivel acadêmico",     
                        } 
                    ),

                    'profissao': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Informe a sua profissão",     
                        } 
                    )
            }

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        exclude = ('estado', 'salario', 'eadmin')
        labels = {
                
                'primeiro_nome':"Primeiro Nome",
                'sobrenome':"Sobrenome",
                'bi':"Bilhete de Identidade",
                'nacionalidade':"Nacionalidade",
                'contacto':"Contacto",
                'sexo':"Sexo",
                'endereco':"Endereço",
                'nivel_academico':"Nivel Academico",
                'profissao': "Profissão",
            }
        widgets = {
                    
                    'primeiro_nome': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o seu nome",     
                        }
                    ),
                    'sobrenome': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o seu sobrenome",     
                        }
                    ),
                    'bilhete': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o seu Bilhete de Identidade",     
                        }
                    ),
                    'nacionalidade': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe a sua nacionalidade",     
                        }
                    ),

                    'contacto': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o seu endereço",     
                        }
                    ),
                   
                    'sexo': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Informe o genero",     
                        } 
                    ),

                    'nivel_academico': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Informe o seu nivel acadêmico",     
                        } 
                    ),
            }

class InstrutorForm(forms.ModelForm):
    class Meta:
        model = Instrutor
        exclude = ('estado', 'salario', 'eadmin')
        labels = {
                
                'primeiro_nome':"Primeiro Nome",
                'sobrenome':"Sobrenome",
                'bi':"Bilhete de Identidade",
                'nacionalidade':"Nacionalidade",
                'contacto':"Contacto",
                'sexo':"Sexo",
                'endereco':"Endereço",
                'nivel_academico':"Nivel Academico",
                'tipo_instrutor': "Tipo Instrutor",
            }
        widgets = {
                    
                    'primeiro_nome': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o seu nome",     
                        }
                    ),
                    'sobrenome': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o seu sobrenome",     
                        }
                    ),
                    'bilhete': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o seu Bilhete de Identidade",     
                        }
                    ),
                    'nacionalidade': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe a sua nacionalidade",     
                        }
                    ),

                    'contacto': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o seu endereço",     
                        }
                    ),
                   
                    'sexo': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Informe o genero",     
                        } 
                    ),

                    'nivel_academico': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Informe o seu nivel acadêmico",     
                        } 
                    ),

                    'tipo_instrutor': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Informe Tipo",     
                        } 
                    )
            }


class MecanicoForm(forms.ModelForm):
    class Meta:
        model = Instrutor
        exclude = ('estado', 'salario', 'eadmin')
        labels = {
                
                'primeiro_nome':"Primeiro Nome",
                'sobrenome':"Sobrenome",
                'bi':"Bilhete de Identidade",
                'nacionalidade':"Nacionalidade",
                'contacto':"Contacto",
                'sexo':"Sexo",
                'endereco':"Endereço",
                'nivel_academico':"Nivel Academico",
                'tipo_mecanico': "Tipo Mecanico",
            }
        widgets = {
                    
                    'primeiro_nome': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o seu nome",     
                        }
                    ),
                    'sobrenome': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o seu sobrenome",     
                        }
                    ),
                    'bilhete': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o seu Bilhete de Identidade",     
                        }
                    ),
                    'nacionalidade': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe a sua nacionalidade",     
                        }
                    ),

                    'contacto': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o seu endereço",     
                        }
                    ),
                   
                    'sexo': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Informe o genero",     
                        } 
                    ),

                    'nivel_academico': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Informe o seu nivel acadêmico",     
                        } 
                    ),

                    'tipo_mecanico': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Informe Tipo",     
                        } 
                    )
            }

