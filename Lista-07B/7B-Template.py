# I. Desenvolver em Python um cadastro de contato usando programação em camadas:
from Model import ContatoDAO

class ContatoUI:
    @classmethod
    def main(ui):
        x = 0
        y = ContatoDAO
        while x != 10:
            x = ui.menu()
            if x == 1: y.inserir()
            if x == 2: y.listar()
            if x == 3: y.listar_id()
            if x == 4: y.atualizar()
            if x == 5: y.excluir()
            if x == 6: y.pesquisar()
            if x == 7: y.aniversariantes()
        
    @classmethod
    def menu(ui):
       return int(input("1-Inserir, 2-listar, 3-listar id, 4-atualizar, 5-excluir, 6-pesquisar, 7-aniversariantes, 8-abrir, 9-salvar, 10-sair "))