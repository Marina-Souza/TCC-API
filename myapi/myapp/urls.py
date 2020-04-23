from django.conf.urls import url, include
from . import views

from django.urls import path, include

urlpatterns = [
    path('', views.home),
    url('admin/', include('myapi.urls')),
    path('historico/', views.ListarAcionamentos.as_view()),
    path('manual/', views.manual),
    path('manual/<pk>/<time>/', views.registra_acionamento),
    path('cadastro/<tipo>/<nome>/<GPIO>', views.registra_dispositivo), #tipo: sensor ou acionador 
    path('condutividade/', views.atualiza_condutividade),
    path('alerta/', views.registra_alerta), #parametro: umidade ou condutividade
]