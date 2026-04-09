dados = {}
pessoas = []
cont = media = soma = 0
while True:
    resp = ' '
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = 'a'
    while dados['sexo'] not in 'MmFf':
        dados['sexo'] = str(input('Sexo [M/f]: ')).strip()[0]
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    cont += 1
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar? [S/n]: ')).strip()[0]
    if resp in 'Nn':
        break
media = soma / cont
print('-'*30)
print(f'- O grupo tem {cont} pessoas')
print(f'- A media de idade entre eles é de {media:.2f}')
print(f'- As mulheres cadastradas foram ',end=' ')
for i, k in enumerate(pessoas):
    if k['sexo'] in 'Ff':
        print(f'{k['nome']}',end=', ')
print()
print(f'As pessoas com idade acima da media de {media:.2f} sao: ',end='')
for i, k in enumerate(pessoas):
    if k['idade'] > media:
        print(f'{k['nome']}',end='')
