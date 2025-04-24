import math
# aula 2 ex 1

fullname = input("digite seu nome completo")
firstname = fullname.split()[0]
print(f'Bem-vindo(a) ao Python, {firstname}')

# ex 2

notabi1 = int(input("digite a nota do seu primeiro bimestre"))
notabi2 = int(input("digite a nota do seu segundo bimestre"))
notatotal = (notabi1 * 2 + notabi2 * 3) / 5
print(f'media parical = {notatotal}')

# ex 3


alt = int(input("digite a base e a altura do retangulo"))
base = int(input())
print(f'Área = {base * alt} - Perímetro = {(base*2) + (alt*2)} - Diagonal = {math.sqrt((alt*alt)+(base*base))}')

#ex 4

fullfrase = input("Digite uma frase:")
print(fullfrase[frase.rindex(" ")+ 1:])

# lista 03 - 1004

x = int(input())
y = int(input())
PROD = x*y
print(f'PROD = {PROD}')

# 1005

A = float(input())
B = float(input())
MEDIA = (A*3.5 + B*7.5)/11
print(f'MEDIA = {MEDIA:.5f}')

# 1011

R = int(input())
VOLUME = 4/3.0 * 3.14159 * R**3
print(f'VOLUME = {VOLUME:.3f}')

# 2416

text = input()
C = int(text.split()[0])
N = int(text.split()[1])
print(C%N)

# 1015

import math

X1Y1 = input()
X2Y2 = input()

x = (float(X2Y2.split()[0]) - float(X1Y1.split()[0]))**2 
y = (float(X2Y2.split()[1]) - float(X1Y1.split()[1]))**2
Distance = math.sqrt(x + y)
print(f'{Distance:.4f}')

# 1930

Concections = input()
T1 = int(Concections.split()[0])
T2 = int(Concections.split()[1])
T3 = int(Concections.split()[2])
T4 = int(Concections.split()[3])
Ttotal = T1 + T2 + T3 + T4 - 3
print(Ttotal)

# lista 04 - 1036

x = input()
a = float(x.split()[0])
b = float(x.split()[1])
c = float(x.split()[2])

delta = (b ** 2) - 4 * a * c

if a == 0:
    print("Impossivel calcular")
elif delta < 0:
    print("Impossivel calcular")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')

# 1044

inp = input()
A = int(inp.split()[0])
B = int(inp.split()[1])
if B%A == 0 or A%B == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

# 1049

nah = input()
pt2 = input()
pt3 = input()
idwin = 0
if pt2 == "ave":
    idwin += 1
if pt2 == "mamifero":
    idwin += 2
if pt2 == "inseto":
    idwin += 3
if pt2 == "anelideo":
    idwin += 4
if pt3 == "carnivoro":
    idwin += 10
if pt3 == "onivoro":
    idwin += 20
if pt3 == "herbivoro":
    idwin += 30
if pt3 == "hematofago":
    idwin += 40
    
    
if idwin == 11:
    print("aguia")
if idwin == 21:
    print("pomba")
if idwin == 22:
    print("homem")
if idwin == 32:
    print("vaca")
    
if idwin == 43:
    print("pulga")
if idwin == 33:
    print("lagarta")
if idwin == 44:
    print("sanguessuga")
if idwin == 24:
    print("minhoca")

# 1050

x = int(input())
if x == 61:
    print("Brasilia")
elif x == 71:
    print("Salvador")
elif x == 11:
    print("Sao Paulo")
elif x == 21:
    print("Rio de Janeiro")
elif x == 32:
    print("Juiz de Fora")
elif x == 19:
    print("Campinas")
elif x == 27:
    print("Vitoria")
elif x == 31:
    print("Belo Horizonte")
else:
    print("DDD nao cadastrado")

# 2424

XeY = input()
X, Y = int(XeY.split()[0]), int(XeY.split()[1])
if 0 <= X <= 432 and 0 <= Y <= 468:
    print("dentro")
else:
    print("fora")
