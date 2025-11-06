class Sla:
    def __init__(self, n, m):
        self.set_numbers(n)
        self.set_string(m)

    def set_numbers(self, n): self.__number = n

    def set_string(self, m): self.__string = m

    def get_string(self): return self.__string
    def get_numbers(self): return self.__number

    def from_dic(dic):
        return Sla(dic["email"], dic["nota"])

list = []

dic = {"1":"string", "2":[1, 2, 3]}
dic2 = {"1":"string2", "2":[4, 5, 6]}
dic3 = {"1":"string3", "2":[7, 8, 9]}
z = 5

list.append(Sla(dic2["1"], dic2["2"]))

z = [z]

for x in list[0].get_numbers():
    z.append(x)
list[0].set_numbers(z)
print(list[0])

"""
list.append(dic)
list.append(dic2)
list.append(dic3)




for x in list:
    nf = 0
    x["2"].append(z)
    for n in x["2"]:
        nf += n
    print(nf/len(x["2"]))
"""