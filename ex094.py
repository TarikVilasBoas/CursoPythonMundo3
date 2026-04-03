dados = {}
pessoas = []
mul = []
cont = media = soma = 0
while True:
    dados[f'nome'] = str(input('Nome: '))
    dados['sexo'] = 'a'
    while dados['sexo'] not in 'MmFf':
        dados[f'sexo'] = str(input('Sexo [M/f]: ')).strip()[0]
    dados[f'idade'] = int(input('Idade: '))
    if dados['sexo'] in 'Ff':
        mul.append(dados['nome'])
        dados['mulher'] = mul.copy()
    pessoas.append(dados.copy())
    cont += 1
    resp = str(input('Deseja continuar? [S/n]: ')).strip()[0]
    if resp in 'Nn':
        break
for c in pessoas:
    soma += c['idade']
media = soma / cont

print('-'*30)
print(f'- O grupo tem {cont} pessoas')
print(f'- A media de idade entre eles é de {media:.2f}')
print(f'- As mulheres cadastradas foram {dados['mulher']}')
print(f'As pessoas com idade acima da media de {media:.2f} sao:')

print('FIM')