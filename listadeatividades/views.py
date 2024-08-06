from django.shortcuts import render
from .models import Atividade

# Create your views here.

def lista_de_atividades(request):
    atividades = Atividade.objects.all()
    return render(request, 'index.html', {'atividades': atividades})