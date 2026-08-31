import sys

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from DatabaseConnection import DatabaseConnection

class CategoriaRepository:
    def __init__(self, id):
        self.conexao =  DatabaseConnection()


    def listar(self):
        sql = '''
            SELECT  id, 
                    descricao
            FROM Categoria 
            ORDER BY descricao
        '''

        conexao = self.conexao
        
        # cria um cursor(), executa o SELECT informado e traz os todos os registros
        self.registros = conexao.cursor().execute(sql).fetchall()

        # define a pagina a ser carregada, adicionando os registros das tabelas 
        return render(request, 'categorias_listar.html', context={'registros': registros})
    
    def buscar_por_id(id):


    def inserir(id_categoria, descricao, preco_unitario, quantidade_estoque):

    
    def atualizar(id, id_categoria, descricao, preco_unitario):


    def excluir(id):