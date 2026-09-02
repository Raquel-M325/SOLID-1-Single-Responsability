from django.shortcuts import render

from .categoria.CategoriaView import CategoriaView
from .produto.ProdutoView import ProdutoView


def categorias(request, acao=None, id=None):
    view = CategoriaView()

    if acao is None:
        return view.exibir_listar(request)
    if acao == 'incluir':
        return view.exibir_incluir(request)
    if acao == 'alterar':
        return view.exibir_alterar(request, id)
    if acao == 'excluir':
        return view.exibir_excluir(request, id)
    if acao == 'salvar':
        return view.exibir_salvar(request)

    return render(request, 'home.html', {'ERRO': 'Ação inválida'})


def produtos(request, acao=None, id=None):
    view = ProdutoView()

    if acao is None:
        return view.exibir_listar(request)
    if acao == 'incluir':
        return view.exibir_incluir(request)
    if acao == 'alterar':
        return view.exibir_alterar(request, id)
    if acao == 'excluir':
        return view.exibir_excluir(request, id)
    if acao == 'salvar':
        return view.exibir_salvar(request)

    return render(request, 'home.html', {'ERRO': 'Ação inválida'})


def home(request):
    return render(request, 'home.html')