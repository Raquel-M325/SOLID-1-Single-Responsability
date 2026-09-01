import sys

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from ProdutoService import ProdutoService
from ProdutoRepository import ProdutoRepository

class ProdutoViewForm(forms.form):
    id = forms.IntegerField(label='ID', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    descricao = forms.CharField(label='Descrição', max_length=30, required=True)
    preco_unitario = forms.DecimalField(label='Preço Unitário', max_digits=10, decimal_places=2, required=True)
    quantidade_estoque = forms.IntegerField(label='Qtd. Estoque', required=True)
    id_categoria = forms.ChoiceField(label='Categoria', required=True)

class ProdutoView:
    def __init__(self):
        self.repository = ProdutoRepository()
        self.service = ProdutoService(self.repository)

    def exibir_listar(self, request, id_categoria):
        registros = self.service.listar()      
          
        return render(request,'produto_listar.html',context={'registros': registros})
    
    def exibir_incluir(request):
        
        return render(request, 'produtos_editar.html', context={'acao': 'Inclusão', 'form': ProdutoViewForm() })
    
    def exibir_alterar(request, id):
        pass

    def exibir_excluir(request, id):
        pass

    def exibir_salvar(request):
        pass
