from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from viatura.models import Viatura
from usuario.models import Funcionario, Aluno, Mecanico, Instrutor
# Create your models here.
TIPO_AULA_MARCACAO = (
    ('Sala', 'Sala'),
    ('Mecânica', 'Mecânica'),
)


TIPO_AULA_PRATICA = (
    ('Condução', 'Condução'),
    ('Mecânica', 'Mecânica'),
)

VIATURA = (
    ('Pesado', 'Pesado'),
    ('Motociclo', 'Motociclo'),
    ('Ligeiro', 'Ligeiro'),
)


class Turma(models.Model):
    nome_turma = models.CharField('Nome Turma',max_length = 100, blank=False, null=False)
    numero_sala = models.PositiveIntegerField('Número Sala',blank=False, null=False)
    hora_inicial = models.PositiveIntegerField('Hora Início', blank=False, null=False)
    hora_final = models.PositiveIntegerField('Hora Termino', blank=False, null=False)
    max_lotacao = models.PositiveIntegerField('Lotação Máxima', blank=False, null=False)
    estado = models.BooleanField('Estado',default=True)
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_actualizacao = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s - %s'%(self.nome_turma, self.numero_sala)

class AulaTeorica(models.Model):
    sumario = models.CharField(max_length = 255, blank=False, null=False)
    # descricao = models.TextField('Descrição',blank=True, null=True)
    # num_sala = models.PositiveIntegerField('Número da Sala', blank=False, null=False)
    hora_inicial = models.PositiveIntegerField('Hora Início', blank=False, null=False)
    hora_final = models.PositiveIntegerField('Hora Termino', blank=False, null=False)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    estado = models.BooleanField('Estado',default=True)
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_actualizacao = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.sumario

class AulaTeoricaAluno(models.Model):
    aulaTeorica = models.OneToOneField(AulaTeorica, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    estado = models.BooleanField('Estado',default=True)
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_actualizacao = models.DateTimeField(auto_now=True, auto_now_add=False)

class AulaPratica(models.Model):
    data_aula_pratica = models.DateField()
    hora_inicial = models.PositiveIntegerField('Hora Início', blank=False, null=False)
    hora_final = models.PositiveIntegerField('Hora Termino', blank=False, null=False)
    tipo_aula_pratica = models.CharField(max_length = 10, default="Condução", blank=False, null=False)
    # turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    estado = models.BooleanField('Estado',default=True)
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_actualizacao = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.tipo_aula_pratica

class MarcarAula(models.Model):
    # dia = models.PositiveIntegerField('Dia', blank=False, null=False)
    # hora_final = models.PositiveIntegerField('Hora', blank=False, null=False)
    tipo_aula = models.CharField(max_length = 10, default="Condução", blank=False, null=False)
    # aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    viatura = models.ForeignKey(Viatura, on_delete=models.CASCADE)
    # turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    estado = models.BooleanField('Estado',default=True)
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_actualizacao = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s %s'%(self.tipo_aula, self.aluno)

class Presenca(models.Model):
    tipo_aula = models.CharField(max_length = 10, choices=TIPO_AULA_PRATICA, blank=False, null=False)
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    dia = models.PositiveIntegerField('Dia', blank=False, null=False)
    estado = models.BooleanField('Estado',default=True)
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_actualizacao = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s %s'%(self.tipo_aula, self.aluno)

class InscreverAula(models.Model):
    
    tipo_aula = models.CharField(max_length = 10, choices=TIPO_AULA_MARCACAO, blank=False, null=False)
    # aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    estado = models.BooleanField('Estado',default=True)
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_actualizacao = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s %s'%(self.tipo_aula - self.aluno)

class PagamentoAula(models.Model):
    tipo_aula = models.CharField(max_length = 10, choices=TIPO_AULA_MARCACAO, blank=False, null=False)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    total_pago = models.PositiveIntegerField('Total Pago', blank=False, null=False)
    estado = models.BooleanField('Estado',default=True)
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_actualizacao = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return '%s %s'%(self.tipo_aula, self.aluno)

class PagamentoTotal(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    total_pago = models.PositiveIntegerField('Total Pago', blank=False, null=False)
    estado = models.BooleanField('Estado',default=True)
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_actualizacao = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s %s'%(self.aluno, self.total_pago)

class Exame(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    total_pago = models.PositiveIntegerField('Total Pago', blank=False, null=False)
    nota_pratica = models.CharField('Nota Pratica',max_length = 100, blank=False, null=False)
    nota_teorica = models.CharField('Nota Teorica',max_length = 100, blank=False, null=False)
    estado = models.BooleanField('Estado',default=True)
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_actualizacao = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s %s'%(self.aluno, self.total_pago)

