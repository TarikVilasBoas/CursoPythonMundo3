numeros = []
par = []
impar = []
while True:
    resp = ' '
    numeros.append(int(input('Digite um numero: ')))
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resp in 'N':
        break

print('*' * 30)
for p in numeros:
    if p % 2 == 0:
        par.append(p)
    else:
        impar.append(p)
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
