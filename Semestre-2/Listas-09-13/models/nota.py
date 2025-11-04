import json

class Nota:
    def __init__(self, nota, email):
        self.set_nota(nota, email)

    def get_nota(self): return self.__nota
    def get_email(self): return self.__email

    def set_nota(self, nota, email):

        self.__nota = NotaDAO.calc_nota(nota, email)
        self.__email = email

    def __str__(self):
        return f"{self.__nota}"

    def to_json(self):
        dic = {"email":self.__email, "nota":self.__nota}
        return dic
    
    @staticmethod
    def from_json(dic):
        return Nota(dic["email"], dic["nota"])



class NotaDAO:
    __list = []


    @classmethod
    def calc_nota(cls, nota, email): #manda para o json todas as notas dadas mas apenas retorna a nota "final"
        __list = cls.listar_email(email)
        if nota != "":
            if nota > 5 or nota < 0: raise ValueError("nota invalida") #not isinstance(nota,(int)): raise ValueError("nota invalida")
            __list.append(nota)

        cls.salvar()
        nf = 0
        for n in __list:
            nf += n
        return nf/len(__list)
        


    @classmethod
    def listar_email(cls, email):
        cls.abrir()
        for x in cls.__list:
            if x.get_email() == email: return x["nota"]
        return None



    @classmethod
    def abrir(cls):
        __list = []
        try:
            with open("AVS.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    x = Nota.from_json(dic)
                    cls.__list.append(x)
        except FileNotFoundError: 
            pass

    @classmethod
    def salvar(cls):
        with open("AVS.json", mode="w") as arquivo:
            json.dump(cls.__list, arquivo, default = Nota.to_json)