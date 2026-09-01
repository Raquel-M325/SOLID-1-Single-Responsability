class CategoriaService:
    def __init__(self, repository):
        self.repository = repository 
        #aqui recebe os dados da view para saber qual acao o usuario fez antes de mandar ao arquivo repository

    def listar(self):
        return self.repository.listar()

    def obter(self, id):
        return self.repository.obter(id)

    def inserir(self, descricao):
        return self.repository.inserir(descricao)

    def atualizar(self, id, descricao):
        return self.repository.atualizar(id, descricao)

    def excluir(self, id):
        return self.repository.excluir(id)
    
    #dependendo das opções, vai mandar os dados para repository de acordo com a acao escolhida
