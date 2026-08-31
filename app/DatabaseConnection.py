import sqlite3

class DatabaseConnection:
    def __init__(self):
        self.conexao = sqlite3.connect('db_solid.sqlite3')

    def conectar(self):
        # comando para não permitir DELETE CASCADE (exclusão em cascata)
        self.conexao.execute("PRAGMA foreign_keys = ON;") 


    def fechar(self):
        self.conexao.close()