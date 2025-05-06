import math

"""
class sla:
    def __init__(self, x):
        self.y = x * 2
    def vezes3(self):
        return self.y * 1.5
    
y = sla(5)

print(y.vezes3())

"""
#ex1:
class Circulo:
    def __init__(self, r):
        self.raio = r
        self.area = (self.raio ** 2)* math.pi
        self.circunf = (math.pi*self.raio*2)
    
x = Circulo(7)
print(x.area)
print(x.circunf)

#ex2:

class distancia:
    def __init__(self, KM, tempoh, tempom):
        Km = KM