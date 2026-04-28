from random import randint
from time import sleep
numeros = []
def sorteia():
    for i in range(5):
        numeros.append(randint(1,6))
    sleep(0.8)
    print(f'Os numeros sorteados sao {numeros}')
def SomaPar():
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {numeros} o total é {soma}')

sorteia()
SomaPar()