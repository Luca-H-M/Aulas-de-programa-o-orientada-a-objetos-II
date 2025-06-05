# aula 9 eu acho
#atividade 1

class Viagem:
    def __init__(self):
        self.__destino = "não definido"
        self.__distancia = 0.0
        self.__litros = 0.0

    def set_destino(self, de):
        try:
            float(de)
            print("Nome invalido")
        except:
            self.__destino = de
    def set_distancia(self, di):
        try:
            float(di)
            self.__distancia = di
        except:
            print("Utilize um numero")
    def set_litros(self, li):
        try:
            float(li)
            self.__litros = li
        except:
            print("Utilize um numero")

    def get_destino(self):
        return self.__destino
    def get_distancia(self):
        return self.__distancia
    def get_litros(self):
        return self.__litros
    
    def consumo(self):
        print(f'Consumo médio de combustivel: {self.__distancia/self.__litros}')

class ViagemUI:
    @staticmethod
    def menu(self):
        self.escolha = input("digite: 1 – Calcular, 2 – Fim")
    
    @staticmethod
    def main(self):
        if self.escholha == 1:
            viagem = Viagem
            viagem.set_destino()
            viagem.set_distancia()
            viagem.set_litros()
            print(viagem.get_destino)
            print(viagem.get_distancia)
            print(viagem.get_litros)
            viagem.consumo()
            ViagemUI.menu()

#atividade 2 seria só mudar os nomes e ao invez de dividir distancia/litros dividiria a "quantidade de pessoas"/km2