cadastro = []
dados = []
mais = menos = 0
while True:
    us = ' '
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(cadastro) == 0:
        mais = menos = dados[1]
    else:
        if dados[1] > mais:
            mais = dados[1]
        if dados[1] < menos:
            menos = dados[1]
    cadastro.append(dados[:])
    dados.clear()
    while us not in 'SsNn':
        us = str(input('Deseja continuar? [S/n]: '))
    if us in 'Nn':
        break
print(f'Foram digitadas {len(cadastro)} pessoas')
print(f'O maior peso foi {mais}kg, peso de ',end=' ')
for p in cadastro:
    if p[1] == mais:
        print(f'{p[0]} ',end=', ')
print()
print(f'O menor peso foi {menos}kg peso de ',end=' ')
for p in cadastro:
    if p[1] == menos:
        print(f'{p[0]} ',end=', ')