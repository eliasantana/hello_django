from django.shortcuts import render, HttpResponse

# Create your views here.
# Recebe nome e idade como parâmetro na requisição
def hello(request, nome, idade):
    return HttpResponse('Hello {} de {} anos'.format(nome, idade))