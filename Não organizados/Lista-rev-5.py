# Questão 1. Escrever a classe do modelo: Treino
class specclass:
    def __init__(self):
        self.__varstr = "data do treino;"
        self.__specvar1 = "id"
        self.__specvar2 = "tempo"
        self.__specvar3 = "distancia"

    def set_varstr(self, de):
        try:
            float(de)
            print("Data invalido")
        except:
            self.__varstr = de
    def set_specvar1(self, de):
        try:
            float(de)
            str(de)
            self.__specvar1 = de
        except:
            print("distancia invalida")
    def set_specvar2(self, de):
        try:
            float(de)
            str(de)
            self.__specvar2 = de
        except:
            print("distancia invalida")
    def set_specvar3(self, de):
        try:
            float(de)
            print("Data invalido")
        except:
            self.__specvar3 = de

    def get_varstr(self):
        return self.__varstr
    def get_specvar1(self):
        return self.__specvar1
    def get_specvar(self):
        return self.__specvar2
    def get_specvar3(self):
        return self.__specvar3

    def __ToString__(self):
        return ('f{get_varstr}, {get_specvar1}, {get_specvar2}, {get_specvar3}')