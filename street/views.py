from django.shortcuts import render
from .models import cliente
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.
class cliente(request):
 
    cliente = Cliente()

    cliente.nome = request.POST.get( 'nome' )
    cliente.email = request.POST.get( 'e-mail' )
    cliente.telefone = request.POST.get('telefone')
    cliente.datanascimento = request.POST.get( 'datanascimento' )
    cliente.nacionalidade = request.POST.get('nationality')
    cliente.salvar()


def checkbox(request):
    cliente.