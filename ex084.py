cadastro = []
dados = []
maisp = []
menosp = []
contp = mais = menos = 0
while True:
    us = ' '
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    cadastro.append(dados[:])
    dados.clear()
    contp += 1
    while us not in 'SsNn':
        us = str(input('Deseja continuar? [S/n]: '))
    if us in 'Nn':
        break
for c in cadastro:
    if c[1] >= 100:
        maisp.append(c[0])
        mais = c[1]
    elif c[1] <= 70:
        menosp.append(c[0])
        menos = c[1]
print(f'Foram digitadas {contp} pessoas')
print(f'O maior peso foi {mais}kg Foram das pessoas: {maisp}')
print(f'O menor peso foi {menos}kg e são das pessoas:  {menosp}')
