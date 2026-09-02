from ..DatabaseConnection import DatabaseConnection

class CategoriaRepository:
    def __init__(self):
        self.conexao = DatabaseConnection()

    def listar(self):
        sql = '''
            SELECT  id, 
                    descricao
            FROM Categoria 
            ORDER BY descricao
        '''

        return self.conexao.executar(sql).fetchall()
    
    def obter(self, id):
        return self.conexao.executar(
            'SELECT id, descricao FROM Categoria WHERE id = ?', (id,)
        ).fetchone()

    def inserir(self, descricao):
        self.conexao.executar(
            'INSERT INTO Categoria (descricao) VALUES (?)', (descricao,)
        )
        self.conexao.confirmar()

    def atualizar(self, id, descricao):
        self.conexao.executar(
            'UPDATE Categoria SET descricao = ? WHERE id = ?', (descricao, id)
        )
        self.conexao.confirmar()

    def excluir(self, id):
        self.conexao.executar('DELETE FROM Categoria WHERE id = ?', (id,))
        self.conexao.confirmar()