from ..DatabaseConnection import DatabaseConnection


class ProdutoRepository:
    def __init__(self):
        self.conexao = DatabaseConnection()

    def listar(self):
        sql = '''
            SELECT pro.id, pro.descricao, pro.preco_unitario,
                   pro.quantidade_estoque, pro.categoria_id,
                   cat.descricao
            FROM Produto pro
            INNER JOIN Categoria cat ON cat.id = pro.categoria_id
            ORDER BY pro.descricao
        '''
        return self.conexao.executar(sql).fetchall()

    def listar_categorias(self):
        return self.conexao.executar(
            'SELECT id, descricao FROM Categoria ORDER BY descricao'
        ).fetchall()

    def obter(self, id):
        return self.conexao.executar(
            '''SELECT pro.id, pro.descricao, pro.preco_unitario,
                      pro.quantidade_estoque, pro.categoria_id,
                      cat.descricao
               FROM Produto pro
               INNER JOIN Categoria cat ON cat.id = pro.categoria_id
               WHERE pro.id = ?''', (id,)
        ).fetchone()

    def inserir(self, descricao, preco_unitario, quantidade_estoque, categoria_id):
        self.conexao.executar(
            '''INSERT INTO Produto
               (descricao, preco_unitario, quantidade_estoque, categoria_id)
               VALUES (?, ?, ?, ?)''',
            (descricao, str(preco_unitario), quantidade_estoque, categoria_id)
        )
        self.conexao.confirmar()

    def atualizar(self, id, descricao, preco_unitario, quantidade_estoque, categoria_id):
        self.conexao.executar(
            '''UPDATE Produto
               SET descricao = ?, preco_unitario = ?, quantidade_estoque = ?,
                   categoria_id = ?
               WHERE id = ?''',
            (descricao, str(preco_unitario), quantidade_estoque, categoria_id, id)
        )
        self.conexao.confirmar()

    def excluir(self, id):
        self.conexao.executar('DELETE FROM Produto WHERE id = ?', (id,))
        self.conexao.confirmar()