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