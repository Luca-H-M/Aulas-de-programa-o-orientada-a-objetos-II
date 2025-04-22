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
