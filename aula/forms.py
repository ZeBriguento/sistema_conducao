from django import forms
#from bootstrap_datepicker_plus.widgets import DatePickerInput
from .models import Presenca, Turma, AulaPratica, AulaTeorica, MarcarAula, InscreverAula, PagamentoAula, PagamentoTotal

# Create your forms here.

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        exclude = ('estado',)
        labels = {
            'nome_turma':"Nome da Turma",
            'numero_sala':"Número da Sala",
            'lotacao_maxima':"Lotação Máxima",
        }
        widgets = {
            
                'nome_turma': forms.TextInput(
                    attrs = {
                        'class':"form-control is-valid",
                        'placeholder':"Digite o nome da turma",     
                    }
                ),
                'numero_sala': forms.TextInput(
                    attrs = {
                        'class':"form-control is-valid",
                        'placeholder':"Digite o número da sala",     
                    }
                ),
                'max_lotacao': forms.TextInput(
                    attrs = {
                        'class':"form-control is-valid",
                        'placeholder':"Digite a lotação máxima permitida",     
                    }
                ),
        }
 
        
    

class AulaPraticaForm(forms.ModelForm):
    class Meta:
        model = AulaPratica
        exclude = ('estado',)
        labels = {
                'data_aula_pratica':"Data de realização",
                'hora_inicial':"Hora de início da aula",
                'hora_final':"Hora de termino da aula",
                'tipo_aula_pratica':"Tipo de aula",
            }
        widgets = {
                    'data_aula_pratica':forms.DateInput(),
                    'hora_inicial': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe a hora de realização da aula",     
                        }
                    ),
                    'hora_final': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe a hora de termino da aula",     
                        }
                    ),
                    'tipo_aula_pratica': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Informe a hora de termino da aula",     
                        } 
                    )
                    
            }

class AulaTeoricaForm(forms.ModelForm):
    class Meta:
        model = AulaTeorica
        exclude = ('estado',)
        labels = {
                'sumario':"Sumário",
                'hora_inicial':"Hora de início da aula",
                'hora_final':"Hora de termino da aula",
                'turma':"Turma",
            }
        widgets = {

                    'sumario': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Digite o sumário",     
                        }
                    ),
                    'hora_inicial': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe a hora de realização da aula",     
                        }
                    ),
                    'hora_final': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe a hora de termino da aula",     
                        }
                    ),
                    'turma': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Informe turma",     
                        } 
                    )
                    
            }

class MarcarAulaForm(forms.ModelForm):
    class Meta:
        model = MarcarAula
        exclude = ('estado', 'tipo_aula')
        labels = {
                'aluno':"Aluno",
                'instrutor':"Instrutor",
                'dia':"Dia da aula",
                'hora_final':"Hora de termino da aula",
                'viatura':"Estado da Viatura",
               
            }
        widgets = {

                     'aluno': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Aluno",     
                        } 
                    
                    ),

                     'instrutor': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Instrutor",     
                        } 
                    
                    ),

                    'viatura': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Viatura",     
                        } 
                    
                    ),


                    'hora_final': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe a hora de realização da aula",     
                        }
                    ),
                    'dia': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o dia da aula",     
                        }
                    ),
                   
                    
            }

class PresencaForm(forms.ModelForm):
    class Meta:
        model = Presenca
        exclude = ('estado', 'tipo_aula')
        labels = {
                'aluno':"Aluno",
                'instrutor':"Instrutor",
            }
        widgets = {

                     'aluno': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Aluno",     
                        } 
                    
                    ),

                     'instrutor': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Instrutor",     
                        } 
                    
                    ),                   
                     'dia': forms.TextInput(
                        attrs = {
                            'class':"form-control is-valid",
                            'placeholder':"Informe o dia da aula",     
                        }
                    ),
            }

class InscreverAulaForm(forms.ModelForm):
    class Meta:
        model = InscreverAula
        exclude = ('estado',)
        labels = {
                
                'turma':"Turma",
                'tipo_aula':"Tipo Aula",
            }
        widgets = {

                    

                     'turma': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Turma",     
                        } 
                    
                    ),   

                    'tipo_aula': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Tipo Aula",     
                        } 
                    
                    ),                   
                    
            }

class PagamentoAulaForm(forms.ModelForm):
    class Meta:
        model = PagamentoAula
        exclude = ('estado',)
        labels = {
                'aluno':"Aluno",
                'tipo_aula':"Tipo Aula",
                'total_aula':"Total Pago",
            }
        widgets = {

                     'aluno': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Aluno",     
                        } 
                    
                    ),

                     'total_pago': forms.TextInput(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Total Pago",     
                        } 
                    
                    ),   

                    'tipo_aula': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Tipo Aula",     
                        } 
                    
                    ),                   
                    
            }


class PagamentoTotalForm(forms.ModelForm):
    class Meta:
        model = PagamentoTotal
        exclude = ('estado',)
        labels = {
                'aluno':"Aluno",
                'total_pago':"Total Pago",
            }
        widgets = {

                     'aluno': forms.Select(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Aluno",     
                        } 
                    
                    ),

                     'total_pago': forms.TextInput(
                       attrs = {
                            'class':"form-select is-valid",
                            'placeholder':"Total Pago",     
                        } 
                    
                    ),                    
                    
            }
