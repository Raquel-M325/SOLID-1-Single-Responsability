import sys

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from CategoriaService import CategoriaService


class CategoriaView:
    def exibir_listar(request):
        
        return render(request, 'categorias_listar.html', context={'registros': registros})

    
    def exibir_incluir(request):

    
    def exibir_alterar(request, id):


    def exibir_excluir(request, id):


    def exibir_salvar(request):
