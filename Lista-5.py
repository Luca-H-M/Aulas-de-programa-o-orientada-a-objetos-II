#1. Um Paciente

class Paciente:
    def __init__(self):
        self.__nome = "não definido"
        self.__CPF = "não definido"
        self.__telefone = "não definido"
        self.__nascimento = "00-00-0000"

    def set_nome(self, de):
        try:
            float(de)
            print("Nome invalido")
        except:
            self.__nome = de
     def set_CPF(self, de):
        try:
            float(de)
            str(de)
            self.__CPF = de
        except:
            print("CPF invalido")

    def set_telefone(self, de):
        try:
            float(de)
            str(de)
            self.__telefone = de
        except:
            print("telefone invalido")

    def set_nascimento(self, de):

        self.__nascimento = de

    def get_nascimento(self):
        return self.__nascimento
    def get_nome(self):
        return self.__nome
    def get_telefone(self):
        return self.__telefone
    def get_CPF(self):
        return self.__CPF
    
    def Idade(self):
        x = 24307.0
        z = 0
        y = 0
        while y < len[self.__nascimento]
            if y > 3 and y != 5
                w = self.__nascimento[y]
                if y > 5:
                    w *= 12
                z += w
            y += 1
        x -= z
        y = 12%x 
        y *= 12
        x /= 12
        print(f'Idade do paciente: {x} anos e {y} meses')

    de ToString(self):
    print(f'Nome: {get_nome} CPF: {get_CPF} nascimento: {get_nascimento} telefone: {get_telefone}')

class PacienteUI:
    @staticmethod
    def menu(self):
        self.escolha = input("digite: 1 – Calcular, 2 – Fim")
    
    @staticmethod
    def main(self):
        if self.escholha == 1:
            paciente = Paciente
            paciente.set_nascimento()
            paciente.set_nome()
            paciente.set_telefone()
            paciente.set_CPF()
            print(paciente.get_nascimento)
            print(paciente.get_telefone)
            print(paciente.get_nome)
            print(paciente.get_CPF)
            paciente.Idade()
            pacienteUI.menu()
