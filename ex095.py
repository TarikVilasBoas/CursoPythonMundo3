dados = {}
gols = []
jogadores = []
cont = 0
while True:
    resp = ' '
    dados['nome'] = str(input('Nome do jogador: '))
    part = int(input(f'Quantas partidas o {dados["nome"]} jogou? '))
    for q in range(part):
        gols.append(int(input(f'Quantos gols na {q+1} partida? ')))
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    jogadores.append(dados.copy())
    gols.clear()
    dados.clear()
    cont += 1
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar? S/n: '))
    if resp in 'Nn':
        break
print('='*40)
print(f'{'Cod':<}{'Nome':^10}{'Gols'}{'Total':>20}')
print('-'*40)
for i, v in enumerate(jogadores):
    print(f'{i} {v['nome']:^10} {v['gols']}  {v['total']:>15}')
while True:
    x = ' '
    print('='*30)
    x = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if x == 999:
        break
    if x >= len(jogadores):
        print(f'Erro: Nao existe jogador com codigo {x}')
    else:
        print('-'*30)
        print(f'Levantamento do jogador {jogadores[x]['nome']}:')
        for i,v in enumerate(jogadores[x]['gols']):
            print(f'No jogo {i+1} ele fez {v} gols  ')
