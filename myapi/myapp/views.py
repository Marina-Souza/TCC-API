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

def atualiza_condutividade(request, limiar):
    sistema, created = Sistema.objects.get_or_create(id=1)
    sistema.condutividade = float(limiar)
    sistema.vazao = 1
    sistema.cronIrrigacao = '* * * * *'
    sistema.umidade = '30'
    sistema.save()
    return JsonResponse({'nome': 'condutividade', 'valor': limiar}, safe=False, status=status.HTTP_200_OK)

def registra_alerta(request, pk, limiar, ativo):
    dispositivo = Dispositivos.objects.get(id=int(pk))
    alerta = Alertas(idDispositivo=dispositivo, limiar=limiar, ativo=ativo)
    alerta.save()
    return JsonResponse({'nome': 'condutividade', 'valor': 'limiar'}, safe=False, status=status.HTTP_200_OK)

def get_values(queryList):
    arr = []
    for item in queryList:
        return arr

def home(request):
    acionadores = Dispositivos.objects.filter(tipo='acionador').values()
    sensores = Dispositivos.objects.filter(tipo='sensor')
    sistema = list(Sistema.objects.filter(id=1).values())[0]
    return render(request, 'home.html', {'acionadores': acionadores, 'sensores': sensores, 'sistema': sistema})

def manual(request):
    return JsonResponse({'nome': 'UHUL'}, safe=False, status=status.HTTP_200_OK)

class index(generics.ListCreateAPIView):
    queryset = Dispositivos.objects.all()

class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

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

