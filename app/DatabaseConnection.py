import sqlite3

class DatabaseConnection:
    def __init__(self):
        self.conexao = sqlite3.connect('db_solid.sqlite3')
        self.conectar()

    def conectar(self):
        # comando para não permitir DELETE CASCADE (exclusão em cascata)
        self.conexao.execute("PRAGMA foreign_keys = ON;") 

    def executar(self, sql, parametros=()):
        return self.conexao.execute(sql, parametros)

    def confirmar(self):
        self.conexao.commit()

    def fechar(self):
        self.conexao.close()