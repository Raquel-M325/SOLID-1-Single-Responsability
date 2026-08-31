import sys

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from CategoriaService import CategoriaService


class CategoriaView: 
    def exibir_listar(request):  #mostra a página de listagem das categorias. Cria uma instância do CategoriaService e solicita os registros cadastrados. Depois, envia os registros para o template categorias_listar.html.        
        service = CategoriaService()
        registros = service.listar()
        return render(request,'categorias_listar.html',context={'registros': registros})

    def exibir_incluir(request):  #exibe o formulário para inclusão de uma nova categoria. A View cria um formulário vazio e informa ao template que a operação que será realizada é uma inclusão.
        return render(
            request,'categorias_editar.html',context={
                'acao': 'Inclusão',
                'form': CategoriaForm()
            }
        )
    #mostra o formulário de alteração de uma categoria. Recebe o ID da categoria, solicita os dados ao CategoriaService e utiliza esses dados para preencher o formulário de alteração.
    def exibir_alterar(request, id):
        service = CategoriaService()

        registro = service.obter(id)

        registro_dict = {
            'id': registro[0],
            'descricao': registro[1]
        }
        return render(request,'categorias_editar.html',
            context={
                'acao': 'Alteração',
                'form': CategoriaForm(initial=registro_dict)
            }
        )
    # Mostrar o formulário de exclusão de uma categoria.Recebe o ID da categoria, busca seus dados através do CategoriaService e apresenta essas informações para que o usuário possa confirmar a exclusão.
    def exibir_excluir(request, id):
        service = CategoriaService()

        registro = service.obter(id)

        registro_dict = {
            'id': registro[0],
            'descricao': registro[1]
        }

        return render(
            request,'categorias_editar.html',
            context={
                'acao': 'Exclusão',
                'form': CategoriaForm(initial=registro_dict)
            }
        )
        #recebe os dados enviados pelo formulário. Identifica se a operação solicitada é uma inclusão, alteração ou exclusão e encaminha a operação correspondente para o CategoriaService.
    def exibir_salvar(request):
        service = CategoriaService()

        form_data = request.POST
        acao = form_data['acao']

        if acao == 'Inclusão': # Se a ação for inclusão, solicita ao Service que cadastre a categoria.
            service.inserir(form_data['descricao'])

        elif acao == 'Alteração':
            service.atualizar(
                form_data['id'],
                form_data['descricao']
            )

        elif acao == 'Exclusão': #vai excluir 
            service.excluir(form_data['id'])

        return HttpResponseRedirect( #manda pra pagina de categorias
            reverse('categorias')
        )