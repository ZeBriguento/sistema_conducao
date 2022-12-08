from django.contrib import admin
from .models import Turma, AulaPratica, AulaTeorica, Presenca, PagamentoTotal, Exame

# Register your models here.
admin.site.register(Turma)
admin.site.register(AulaPratica)
admin.site.register(AulaTeorica)
admin.site.register(Presenca)
admin.site.register(PagamentoTotal)
admin.site.register(Exame)
