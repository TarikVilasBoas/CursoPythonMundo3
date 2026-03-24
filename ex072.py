from num2words import num2words
num = tuple(range(0,21))
us = 0
escrita = resp = ' '
while True:
    us = int(input('Digite um numero entre 0 e 20: '))
    if us in num:
        pos = num.index(us)
        escrita = num2words(num[pos], lang='pt_BR')
        print(f'O numero digitado foi {escrita}')
        while resp not in 'SN':
            resp = str(input('Deseja ver mais numeros? S/N: ')).strip().upper()
        if resp == 'N':
            break
        resp = ' '
    else:
        print('Valor incorreto, digite novamente.')

