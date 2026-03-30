from random import randint
from time import sleep
numeros = []
pc = []
print(f'{'JOGO DA LOTERIA':*^50}')
print('-'*50)
j = int(input('Quantos jogos voce quer que eu sorteie? '))
for e in range(j):
    for n in range(6):
        pc.append(randint(0,61))
    numeros.append(pc[:])
    pc.clear()
print('='*50)
for n in range(len(numeros)):
    numeros[n].sort()
    print(f'Jogo {n+1} = {numeros[n]}')
    sleep(0.7)
