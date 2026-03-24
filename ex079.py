numeros = []
us = ' '
while us not in 'N':
    us = ' '
    num = int(input('Digite um valor: '))
    if num in numeros:
        print('Valor Duplicado, nao sera add')
    else:
        numeros.append(num)
        print('Valor add...')
    while us not in 'SN':
        us = str(input('Deseja continuar? s/n: ')).upper().strip()[0]
print(f'Os valores digitados foram {sorted(numeros)}')

