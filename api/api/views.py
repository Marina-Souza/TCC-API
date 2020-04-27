from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from django.http import JsonResponse

def home(request):
    nome = 'Marina'
    return render(request, 'home.html', {'user': nome})