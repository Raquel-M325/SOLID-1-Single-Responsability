class ProdutoService:
    def __init__(self, repository):
        self.repository = repository

    def listar(self):
        return self.repository.listar()

    def obter(self, id):
        return self.repository.obter(id)

    def listar_categorias(self):
        return self.repository.listar_categorias()

    def inserir(self, descricao, preco_unitario, quantidade_estoque, categoria_id):
        return self.repository.inserir(
            descricao, preco_unitario, quantidade_estoque, categoria_id
        )

    def atualizar(self, id, descricao, preco_unitario, quantidade_estoque, categoria_id):
        return self.repository.atualizar(
            id, descricao, preco_unitario, quantidade_estoque, categoria_id
        )

    def excluir(self, id):
        return self.repository.excluir(id)