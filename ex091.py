from random import randint
from time import sleep
from operator import itemgetter
dados = {}
rank = {}
for j in range(1,5):
    dados[f'Jogador{j}'] = randint(1,6)
for i,d in dados.items():
    print(f'O {i} tirou {d}')
    sleep(0.5)
print('-_'*30)
rank = sorted(dados.items(), key=itemgetter(1), reverse=True)
for i, d in enumerate(rank):
    print(f'Em {i+1} lugar o {d[0]} com {d[1]}')
    sleep(0.6)