from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from .CategoriaService import CategoriaService
from .CategoriaRepository import CategoriaRepository


class CategoriaViewForm(forms.Form):
    id = forms.IntegerField(label='ID',widget=forms.TextInput(attrs={'readonly': 'readonly'}),required=False)
    descricao = forms.CharField(label='Descrição',max_length=30,required=True)

class CategoriaView:
    def __init__(self):
        self.repository = CategoriaRepository()
        self.service = CategoriaService(self.repository)

    def exibir_listar(self, request):
        registros = self.service.listar()

        return render(request,'categorias_listar.html',context={'registros': registros})

    def exibir_incluir(self, request):
        return render(request,'categorias_editar.html',context={'acao': 'Inclusão','form': CategoriaViewForm()})

    def exibir_alterar(self, request, id):
        registro = self.service.obter(id)

        registro_dict = {
            'id': registro[0],
            'descricao': registro[1]
        }

        return render(request,'categorias_editar.html',context={'acao': 'Alteração','form': CategoriaViewForm(initial=registro_dict)})

    def exibir_excluir(self, request, id):
        registro = self.service.obter(id)

        registro_dict = {
            'id': registro[0],
            'descricao': registro[1]
        }

        return render(request,'categorias_editar.html',context={'acao': 'Exclusão','form': CategoriaViewForm(initial=registro_dict)})

    def exibir_salvar(self, request):
        form_data = request.POST
        acao = form_data['acao']

        if acao == 'Inclusão':
            self.service.inserir(form_data['descricao'])

        elif acao == 'Alteração':
            self.service.atualizar(
                form_data['id'],
                form_data['descricao']
            )

        elif acao == 'Exclusão':
            self.service.excluir(form_data['id'])

        return HttpResponseRedirect(reverse('categorias'))
