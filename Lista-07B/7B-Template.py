# I. Desenvolver em Python um cadastro de contato usando programação em camadas:
from View import View

class ContatoUI:
    @classmethod
    def main(ui):
        x = 0
        y = View
        while x != 10:
            x = ui.menu()
            if x == 1: y.Contato_inserir()
            if x == 2: y.Contato_listar()
            if x == 3: y.Contato_listar_id()
            if x == 4: y.Contato_atualizar()
            if x == 5: y.Contato_excluir()
            if x == 6: y.Contato_pesquisar()
            if x == 7: y.Contato_aniversariantes()
        
    @classmethod
    def menu(ui):
       return int(input("1-Inserir, 2-listar, 3-listar id, 4-atualizar, 5-excluir, 6-pesquisar, 7-aniversariantes, 8-abrir, 9-salvar, 10-sair "))