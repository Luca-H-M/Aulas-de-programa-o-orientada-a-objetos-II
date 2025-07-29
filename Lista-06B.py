# I. Desenvolver em Python um cadastro de contatos:
from datetime import datetime
import json

class Contato:
    def __init__(self):
        self.__nome = "nome"
        self.__id = "id"
        self.__email = "email"
        self.__fone = "fone"
        self.__nascimento = datetime.today()

    def set_nome(self, de):
        try:
            float(de)
            print("nome invalido")
        except:
            self.__nome = de
    def set_id(self, de):
        try:
            float(de)
            str(de)
            self.__id = de
        except:
            print("id invalida")
    def set_email(self, de):
        try:
            float(de)
            print("email invalido")
        except:
            self.__email = de
    def set_fone(self, de):
        try:
            float(de)
            print("fone invalido")
        except:
            self.__fone = de
    def set_nascimento(self, de):
        try:
            de = datetime.strptime(de, "%Y, %m, %d")
            self.__nascimento = datetime.date(de)
        except:
            print("nascimento invalido")

    def get_nome(self):
        return self.__nome
    def get_id(self):
        return self.__id
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone
    def get_nascimento(self):
        return self.__nascimento

    def __str__(self):
        return (f'{self.__id} ,{self.__nome} , {self.__email}, {self.__fone}, {self.__nascimento}')
    
    def contato(self):
        x = {}
        x["id"] = self.__id    
        x["nome"] = self.__nome
        x["email"] = self.__email
        x["nascimento"] = self.__nascimento
        x["fone"] = self.__fone
        print(x)
        return x
    
class ContatoUI:
    __contatos = []
    @classmethod
    def main(ui):
        x = 0
        while x != 10:
            x = ui.menu()
            if x == 1: ui.inserir()
            if x == 2: ui.listar()
            if x == 3: ui.listar_id()
            if x == 4: ui.atualizar()
            if x == 5: ui.excluir()
            if x == 6: ui.pesquisar()
            if x == 7: ui.aniversariantes()
            if x == 8: ui.abrir()
            if x == 9: ui.salvar()
        
    @classmethod
    def menu(ui):
       return int(input("1-Inserir, 2-listar, 3-listar id, 4-atualizar, 5-excluir, 6-pesquisar, 7-aniversariantes, 8-abrir, 9-salvar, 10-sair "))

    @classmethod
    def inserir(ui):
        x = Contato()
        x.set_id(input("id"))
        x.set_nome(input("nome"))
        x.set_email(input("email"))
        x.set_nascimento(input("nascimento: ano, mês, dia"))
        x.set_fone(input("fone"))
        ui.__contatos.append(x)

    @classmethod
    def listar(ui):
        for x in ui.__contatos:
            print(x)
    
    @classmethod
    def listar_id(ui):
        z = input("id")
        for x in ui.__contatos:
            if x.get_id().startswith(z):
                print (x)

    @classmethod
    def atualizar(ui):
        for x in ui.__contatos:
            if x.get_id() == int(input("informe o id do contato que deseja atualizar:")):
                x.set_nome(input("nome"))
                x.set_email(input("email"))
                x.set_nascimento("nascimento")
                x.set_fone("fone")
                print("contato atualizado")
                return
            else: 
                print("id invalido")

    @classmethod
    def excluir(ui):
        y = input("informe o id do contato que deseja excluir:")
        for x in ui.__contatos:
            if x.get_id() == y:
                ui.__contatos.remove(x)

    @classmethod
    def pesquisar(ui):
        x = input("Informe o nome: ")
        for y in ui.__contatos:
            if y.get_nome().startswith(x):
                print(y)

    @classmethod
    def aniversariantes(ui):
        y = input("Informe o mês")
        for x in ui.__contatos:
            if x.get_nascimento().month == y:
                print(x)

    @classmethod
    def abrir(ui):
        pass

    @classmethod
    def salvar(ui):
        x = Contato()
        with open("contatos.json", mode="w") as arquivo:
            json.dump(ui.__contatos, arquivo, default = Contato.contato)