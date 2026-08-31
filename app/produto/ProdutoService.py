import sys

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

class ProdutoService:
    def __init__(self, id_categoria, id, descricao, preco_unitario, quantidade_estoque):
        self.id = id
        self.id_categoria = id_categoria
        self.descricao = descricao
        self.preco_unitario = preco_unitario
        self.quantidade_estoque = quantidade_estoque


    def listar(self, request):
        
    
    def obter(self, id):


    def inserir(self, id_categoria, descricao, preco_unitario, quantidade_estoque):

    
    def atualizar(self, id, descricao):


    def excluir(self, id):