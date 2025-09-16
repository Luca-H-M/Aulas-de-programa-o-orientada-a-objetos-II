#Lista-1
import random

#ex1:

x = random.randint(-10, 10)
y = random.randint(-10, 10)

if x > y: 
    print(f'maior = {x}')
elif x == y:
    print (f'Numeros iguais')
else:
    print (f'maior = {y}')