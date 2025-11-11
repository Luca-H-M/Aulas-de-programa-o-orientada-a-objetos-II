import json

class Nota:
    def __init__(self, nota, email):
        self.set_nota(nota)
        self.set_email(email)

    def get_nota(self): 
        nf = 0
        if len(self.__nota) > 1:
            for x in self.__nota:
                nf += x
            return nf/len(self.__nota)
        else: return "N/a"
    def get_notas(self): return self.__nota
    def get_email(self): return self.__email

    def set_nota(self, nota): 
        z = []
        for x in nota:
            if x == "": pass
            else: z.append(x)
        
        self.__nota = nota
    def set_email(self, email): self.__email = email


    def __str__(self):
        return f"{self.__nota}"

    def to_json(self):
        dic = {"email":self.__email, "nota":self.__nota}
        return dic
    
    @staticmethod
    def from_json(dic):
        return Nota(dic["nota"], dic["email"])



class NotaDAO:
    __list = []


    @classmethod
    def calc_nota(cls, nota, email): #manda para o json todas as notas dadas (+ email) mas apenas retorna a nota "final"
        cls.listar_email(email)

        if nota != "": #                                                                  ou seja, toda vez que for inserida uma nota
            if nota > 5 or nota < 0 or not isinstance(nota,(int)): raise ValueError("nota invalida") # e a nota seja valida
            if cls.__list == [] or cls.__list[0].get_nota == [""]: #não tem coisas anteriores ou não tem nota anterior
                cls.__list = []
                cls.__list.append(Nota(nota, email)) # lista vai dar append em uma Nota nova
                cls.salvar()
            else: # tem nota valida e tem coisas anteriores
                z = [nota]
                for x in cls.__list[0].get_notas:
                    z.append(x)
                cls.__list[0].set_nota(z)
                cls.salvar()
        elif cls.__list == []: #nota não foi inserida e não existe lista anterior
            cls.__list.append(Nota(nota, email))
            cls.salvar()
        else: #nota não foi inserida e com lista anterior
           x = cls.__list[0].get_nota()
           return x



    @classmethod
    def listar_email(cls, email):
        cls.abrir()
        for x in cls.__list:
            if x.get_email() == email: cls.__list = []; cls.__list.append(x)
        return None


    @classmethod
    def abrir(cls):
        cls.__list = []
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