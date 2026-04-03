dados = {}
gols = []
dados['nome'] = str(input('Nome do jogador: '))
part = int(input('Quantas partidas ele jogou? '))
for q in range(part):
    gols.append(int(input(f'Quantos gols na {q+1} partida? ')))
dados['gols'] = gols.copy()
dados['total'] = sum(gols)
print('=*'*30)
for i, v in dados.items():
    print(f'O campo {i} tem o valor {v}.')
print('=*'*30)
print(f'O jogador {dados['nome']} jogou {part} partidas')
for i in range(part):
    print(f'=> Na partida {i+1} ele fez {gols[i]} gols')
print(f'Foi um total de {dados['total']} gols')