from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def pacotes(request):
    return render(request, 'pacotes.html')

def noticia(request):
    return render(request, 'noticia.html')

def contato(request):
    return render(request, 'contato.html')