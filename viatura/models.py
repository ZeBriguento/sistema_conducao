from django.db import models
ESTADO = (
    ('Bom', 'Bom'),
    ('Danificado', 'Danificado'),
    ('Em Reparação', 'Em Reparação'),
)
# Create your models here.
class Viatura(models.Model):
    nome = models.CharField(max_length = 100, blank=False, null=False)
    estado_viatura = models.CharField(max_length = 30, choices=ESTADO, blank=False, null=False)
    # turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    estado = models.BooleanField('Estado',default=True)
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_actualizacao = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.nome