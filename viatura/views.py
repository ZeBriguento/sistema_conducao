from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import Viatura
from .forms import ViaturaForm
# Create your views here.
class ViaturaListView(ListView):
    model = Viatura
    template_name = "viatura/listar_viatura.html"
    context_object_name = 'viaturas'
    queryset = Viatura.objects.filter(estado = True)

class CriarViaturaView(CreateView):
    model = Viatura
    template_name = "viatura/criar_viatura.html"
    form_class = ViaturaForm
    success_url = reverse_lazy('viatura:listar_viatura')
