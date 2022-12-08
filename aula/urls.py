from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'aula'

urlpatterns = [
    path('criar_turma/', views.CriarTurmaView.as_view(), name='criar_turma'),
    path('listar_turma/', views.TurmaListView.as_view(), name='listar_turma'),

    path('criar_aula_teorica/', views.CriarTeoricaView.as_view(), name='criar_teorica'),
    path('listar_aula_teorica/', views.AulaTeoricaListView.as_view(), name='listar_teorica'),
    
    path('criar_aula_pratica/', views.CriarPraticaView.as_view(), name='criar_pratica'),
    path('listar_aula_pratica/', views.AulaPraticaListView.as_view(), name='listar_pratica'),

    path('listar_marcacao_aula/', views.MarcarAulaListView.as_view(), name='listar_marcacao'),
    path('criar_marcacao_aula/', views.CriarMarcarAulaView.as_view(), name='criar_marcacao'),
    
    path('listar_presenca/', views.PresencaAulaListView.as_view(), name='listar_presenca'),
    path('criar_presenca/', views.CriarPresencaAulaView.as_view(), name='criar_presenca'),

    path('listar_inscrever/', views.InscreverAulaListView.as_view(), name='listar_inscrever'),
    path('criar_inscrever/', views.CriarInscreverAulaView.as_view(), name='criar_inscrever'),

    path('listar_pagamento_aula/', views.PagamentoAulaListView.as_view(), name='listar_pagamento_aula'),
    path('criar_pagamento_aula/', views.CriarPagamentoAulaView.as_view(), name='criar_pagamento_aula'),

    path('listar_pagamento_total/', views.PagamentoTotalListView.as_view(), name='listar_pagamento_total'),
    path('criar_pagamento_total/', views.CriarPagamentoTotalView.as_view(), name='criar_pagamento_total'),
]