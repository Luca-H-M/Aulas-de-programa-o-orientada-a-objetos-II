# I. Desenvolver em Python um cadastro de contato usando programação em camadas:
from Model import ContatoDAO

class View:
    def __init__(self):
        self.x = ContatoDAO
    def Contato_inserir(self):
        return self.x.inserir
    def Contato_listar(self):
        return self.x.listar()
    def Contato_listar_id(self):
        return self.x.listar_id()
    def Contato_atualizar(self):
        return self.x.atualizar()
    def Contato_excluir(self):
        return self.x.excluir()
    def Contato_pesquisar(self):
        return self.x.pesquisar()
    def Contato_aniversariantes(self):
        return self.x.aniversariantes()
