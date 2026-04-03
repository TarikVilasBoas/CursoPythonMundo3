from random import randint
dados = {}
for j in range(1,5):
    dados[f'Jogador{j}'] = randint(1,6)
for i,d in dados.items():
    print(f'O {i} tirou {d}')

print(dados)