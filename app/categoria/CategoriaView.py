import sys

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from CategoriaService import CategoriaService


class CategoriaView:
    def exibir_listar(request):
        service = CategoriaService()

        registros = service.listar()

        return render(request,'categorias_listar.html',context={'registros': registros})

    
    def exibir_incluir(request):
        return render(
            request,'categorias_editar.html',context={
                'acao': 'Inclusão',
                'form': CategoriaForm()
            }
        )
    
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

    def exibir_salvar(request):
        service = CategoriaService()

        form_data = request.POST
        acao = form_data['acao']

        if acao == 'Inclusão':
            service.inserir(form_data['descricao'])

        elif acao == 'Alteração':
            service.atualizar(
                form_data['id'],
                form_data['descricao']
            )

        elif acao == 'Exclusão':
            service.excluir(form_data['id'])

        return HttpResponseRedirect(
            reverse('categorias')
        )