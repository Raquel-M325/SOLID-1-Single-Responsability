from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from .ProdutoService import ProdutoService
from .ProdutoRepository import ProdutoRepository

class ProdutoViewForm(forms.Form):
    id = forms.IntegerField(label='ID', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    descricao = forms.CharField(label='Descrição', max_length=30, required=True)
    preco_unitario = forms.DecimalField(label='Preço Unitário', max_digits=10, decimal_places=2, required=True)
    quantidade_estoque = forms.IntegerField(label='Qtd. Estoque', required=True)
    categoria_id = forms.ChoiceField(label='Categoria', required=True)

class ProdutoView:
    def __init__(self):
        self.repository = ProdutoRepository()
        self.service = ProdutoService(self.repository)

    def exibir_listar(self, request):
        registros = self.service.listar()
          
        return render(request, 'produtos_listar.html', context={'registros': registros})
    
    def _formulario(self, data=None, initial=None):
        form = ProdutoViewForm(data=data, initial=initial)
        form.fields['categoria_id'].choices = self.service.listar_categorias()
        return form

    def exibir_incluir(self, request):
        return render(request, 'produtos_editar.html',
                      context={'acao': 'Inclusão', 'form': self._formulario()})
    
    def exibir_alterar(self, request, id):
        registro = self.service.obter(id)
        initial = self._initial(registro)
        return render(request, 'produtos_editar.html',
                      context={'acao': 'Alteração', 'form': self._formulario(initial=initial)})

    def exibir_excluir(self, request, id):
        registro = self.service.obter(id)
        initial = self._initial(registro)
        return render(request, 'produtos_editar.html',
                      context={'acao': 'Exclusão', 'form': self._formulario(initial=initial)})

    def _initial(self, registro):
        return {
            'id': registro[0],
            'descricao': registro[1],
            'preco_unitario': registro[2],
            'quantidade_estoque': registro[3],
            'categoria_id': registro[4],
        }

    def exibir_salvar(self, request):
        form_data = request.POST
        acao = form_data['acao']

        if acao == 'Exclusão':
            self.service.excluir(form_data['id'])
        else:
            form = self._formulario(data=form_data)
            if form.is_valid():
                dados = form.cleaned_data
                if acao == 'Inclusão':
                    self.service.inserir(
                        dados['descricao'], dados['preco_unitario'],
                        dados['quantidade_estoque'], dados['categoria_id']
                    )
                elif acao == 'Alteração':
                    self.service.atualizar(
                        dados['id'], dados['descricao'], dados['preco_unitario'],
                        dados['quantidade_estoque'], dados['categoria_id']
                    )

        return HttpResponseRedirect(reverse('produtos'))
