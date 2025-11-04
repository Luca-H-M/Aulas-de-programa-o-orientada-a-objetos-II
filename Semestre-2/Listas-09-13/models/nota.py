import json

class Nota:
    def set_nota(self, nota):
        if not isinstance(nota,(int)) or nota > 5 or nota < 0: raise ValueError("nota invalida")
        qtd_avs = []
        qtd_avs.append(self.abrir())
        qtd_avs.append(nota)
        nt = 0
        for x in qtd_avs:
            nt += x
        self.__nota = nt/qtd_avs
        self.__nota = (nota + self.__nota)
        for x in self.qtd_avs:
            dic = {"id":self.__id}
        with open("AVS.json", mode="w") as arquivo:
            json.dump()

    @classmethod
    def abrir(cls):
        list = []
        with open("AVS.json", mode="r") as arquivo:
            list_dic = json.load(arquivo)
            for dic in list_dic:
                if dic["email"] == self.get_email():
                    return list.append(dic)