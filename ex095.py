dados = {}
gols = []
jogadores = []
while True:
    resp = ' '
    dados['nome'] = str(input('Nome do jogador: '))
    part = int(input(f'Quantas partidas o {dados["nome"]} jogou? '))
    for q in range(part):
        gols.append(int(input(f'Quantos gols na {q+1} partida? ')))
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    jogadores.append(dados.copy())
    dados.clear()
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar? S/n: '))
    if resp in 'Nn':
        break
print('='*40)
print(f'{'Cod':<}{'Nome':^10}{'Gols'}{'Total de Gols':>20}')
print('-'*40)
for i, v in enumerate(jogadores):
    print(f'{i} {v['nome']:^10} {v['gols']}  {v['total']:>10}')
