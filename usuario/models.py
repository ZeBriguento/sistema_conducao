from django.db import models

TIPO_AULA_PRATICA = (
    ('Condução', 'Condução'),
    ('Aula Teorica', 'Aula Teorica'),
)

NIVEL_ACADEMICO = (
    
    ('Tecnico Médio', 'Tecnico Médio'),
    ('Licenciado', 'Licenciado'),
    ('Mestrado', 'Mestrado'),
    ('Doctorado', 'Doctorado'),
    ('Outro', 'Outro'),
)

SEXO = (
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
)
TIPO_MECANICO = (
    ('Motociclo', 'Motociclo'),
    ('Pesado', 'Pesado'),
    ('Todos', 'Todos'),
    
)

class Pessoa(models.Model):
    primeiro_nome = models.CharField(verbose_name="Primeiro Nome", max_length = 100, null=False, blank=False)
    sobrenome = models.CharField(max_length = 100, null=False, blank=False)
    bi = models.CharField(verbose_name="Bilhete de Identidade" ,max_length = 50, blank=False, null=False)
    nacionalidade = models.CharField(max_length = 150, blank=False, null=False)
    contacto = models.CharField(max_length = 50, null=False, blank=False)
    sexo = models.CharField(max_length = 100, choices=SEXO,blank=False, null=False)
    endereco = models.CharField(verbose_name="Residência", max_length = 150, blank=True ,null=True)
    nivel_academico = models.CharField("Nível Academico", max_length = 100, null=False, blank=False, choices=NIVEL_ACADEMICO)
    estado = models.BooleanField('Estado',default=True)
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_actualizacao = models.DateTimeField(auto_now=True, auto_now_add=False)


# Create your models here.
class Aluno(Pessoa):
    profissao = models.CharField(max_length = 150, null=False, blank=False)

    def __str__(self):
        return "%s %s"%(self.primeiro_nome, self.sobrenome)

class Funcionario(Pessoa):
    eAdmin = models.BooleanField('Administrador', default=False)
    salario = models.IntegerField(default = 0)
    
    class Meta:
       verbose_name = 'Funcionario'
       verbose_name_plural = 'Funcionarios'

    def __str__(self):
       return '%s %s'%(self.primeiro_nome, self.sobrenome)
    
class Instrutor(Funcionario):
    tipo_instrutor = models.CharField("Tipo instrutor", max_length=100, choices=TIPO_AULA_PRATICA)

    class Meta:
       verbose_name = 'Instrutor'
       verbose_name_plural = 'Instrutores'

    def __str__(self):
           return '%s %s'%(self.primeiro_nome, self.sobrenome)
    
class Mecanico(Funcionario):
    tipo_mecanico = models.CharField(max_length = 100, choices=TIPO_MECANICO, blank=False, null=False)
    class Meta:
       verbose_name = 'Mecânico'
       verbose_name_plural = 'Mecânicos'
    
    def __str__(self):
           return '%s %s'%(self.primeiro_nome, self.sobrenome)
     