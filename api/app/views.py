from rest_framework import generics, status
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.shortcuts import render
from datetime import date
from .models import *
from .serializers import *
from django.http import JsonResponse

# Create your views here.

def registra_acionamento(request, pk, time=1):
    acionamento = Acionamentos()
    acionamento.idDispositivo = Dispositivos.objects.get(id=pk)
    acionamento.valor = time
    acionamento.modo = 'Manual'
    acionamento.save()
    return JsonResponse('Sucesso!', safe=False, status=status.HTTP_200_OK)

def registra_dispositivo(request, tipo, nome, GPIO):
    dispositivo = Dispositivos()
    dispositivo.nome = nome
    dispositivo.tipo = tipo
    dispositivo.GPIOPort = GPIO
    dispositivo.save()
    return JsonResponse({'nome': nome, 'GPIOPort': GPIO}, safe=False, status=status.HTTP_200_OK)

def atualiza_condutividade(request):
    sistema, created = Sistema.objects.get_or_create(id=1)
    sistema.condutividade = float(request.GET["condutividade"])
    sistema.vazao = 1
    sistema.cronIrrigacao = '* * * * *'
    sistema.umidade = '70'
    sistema.ativo = request.GET["ativo"] == 'true'
    sistema.save()
    return JsonResponse({'status': 'sucesso'}, safe=False, status=status.HTTP_200_OK)

def registra_alerta(request):
    alerta, created = Alertas.objects.get_or_create(tipo=request.GET['tipo'])
    alerta.limiar = request.GET['valor']
    alerta.ativo = request.GET['valor'] == 'true'
    alerta.save()
    return JsonResponse({'nome': 'condutividade', 'valor': 'limiar'}, safe=False, status=status.HTTP_200_OK)

def get_values(queryList):
    arr = []
    for item in queryList:
        return arr

def home(request):
    acionadores = Dispositivos.objects.filter(tipo='acionador').values()
    sensores = Dispositivos.objects.filter(tipo='sensor')
    #sistema = list(Sistema.objects.filter(id=1).values())[0] or ''
    return render(request, 'home.html', {'acionadores': acionadores, 'sensores': sensores}  )

def manual(request):
    return JsonResponse({'nome': 'UHUL'}, safe=False, status=status.HTTP_200_OK)

class index(generics.ListCreateAPIView):
    queryset = Dispositivos.objects.all()

class ListarDispositivos(generics.ListCreateAPIView):
    queryset = Dispositivos.objects.all()
    serializer_class = DispositivosSerializer
    objects = models.Manager()

class ListarAcionamentos(generics.ListCreateAPIView):
    queryset = Acionamentos.objects.all()
    model = Acionamentos
    serializer_class = AcionamentosSerializer
    objects = models.Manager()

class CriarAcionamentos(CreateView):
    queryset = Acionamentos.objects.all()
    model = Acionamentos
    serializer_class = AcionamentosSerializer
    objects = models.Manager()
    fields = '__all__'

