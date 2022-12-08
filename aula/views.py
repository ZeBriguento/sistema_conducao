from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .forms import TurmaForm, AulaPraticaForm, AulaTeoricaForm, MarcarAulaForm, PresencaForm, InscreverAulaForm, PagamentoAulaForm, PagamentoTotalForm
from .models import Turma, AulaPratica, AulaTeorica, MarcarAula,Presenca, InscreverAula, PagamentoAula, PagamentoTotal

# Create your views here.

class CriarTurmaView(CreateView):
    model = Turma
    template_name = "aula/criar_turma.html"
    form_class = TurmaForm
    success_url = reverse_lazy('aula:listar_turma')

class TurmaListView(ListView):
    model = Turma
    template_name = "aula/listar_turma.html"
    context_object_name = 'turmas'
    queryset = Turma.objects.filter(estado = True)

class CriarPraticaView(CreateView):
    model = AulaPratica
    template_name = "aula/criar_pratica.html"
    form_class = AulaPraticaForm
    success_url = reverse_lazy('aula:listar_pratica')

class AulaPraticaListView(ListView):
    model = AulaPratica
    template_name = "aula/listar_pratica.html"
    context_object_name = 'praticas'
    queryset = AulaPratica.objects.filter(estado = True)

class CriarTeoricaView(CreateView):
    model = AulaTeorica
    template_name = "aula/criar_teorica.html"
    form_class = AulaTeoricaForm
    success_url = reverse_lazy('aula:listar_teorica')

class AulaTeoricaListView(ListView):
    model = AulaTeorica
    template_name = "aula/listar_teorica.html"
    context_object_name = 'teoricas'
    queryset = AulaTeorica.objects.filter(estado = True)


class MarcarAulaListView(ListView):
    model = MarcarAula
    template_name = "aula/listar_marcacao.html"
    context_object_name = 'marcacoes'
    queryset = MarcarAula.objects.filter(estado = True)


class CriarMarcarAulaView(CreateView):
    model = MarcarAula
    template_name = "aula/criar_marcacao.html"
    form_class = MarcarAulaForm
    success_url = reverse_lazy('aula:listar_marcacao')

class PresencaAulaListView(ListView):
    model = Presenca
    template_name = "aula/listar_presenca.html"
    context_object_name = 'presencas'
    queryset = Presenca.objects.filter(estado = True)

class CriarPresencaAulaView(CreateView):
    model = Presenca
    template_name = "aula/criar_presenca.html"
    form_class = PresencaForm
    success_url = reverse_lazy('aula:listar_presenca')

#
class InscreverAulaListView(ListView):
    model = InscreverAula
    template_name = "aula/listar_inscrever.html"
    context_object_name = 'inscritos'
    queryset = InscreverAula.objects.filter(estado = True)

class CriarInscreverAulaView(CreateView):
    model = InscreverAula
    template_name = "aula/criar_inscrever.html"
    form_class = InscreverAulaForm
    success_url = reverse_lazy('aula:listar_inscrever')
#
class PagamentoAulaListView(ListView):
    model = PagamentoAula
    template_name = "aula/listar_pagamento_aula.html"
    context_object_name = 'pagamentos'
    queryset = PagamentoAula.objects.filter(estado = True)

class CriarPagamentoAulaView(CreateView):
    model = PagamentoAula
    template_name = "aula/criar_pagamento_aula.html"
    form_class = PagamentoAulaForm
    success_url = reverse_lazy('aula:listar_pagamento_aula') 

#
class PagamentoTotalListView(ListView):
    model = PagamentoTotal
    template_name = "aula/listar_pagamento_total.html"
    context_object_name = 'pagamentos'
    queryset = PagamentoTotal.objects.filter(estado = True)

class CriarPagamentoTotalView(CreateView):
    model = PagamentoTotal
    template_name = "aula/criar_pagamento_total.html"
    form_class = PagamentoTotal
    success_url = reverse_lazy('aula:listar_pagamento_total') 
