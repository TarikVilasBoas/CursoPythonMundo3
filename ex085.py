numeros = []
par = []
impar = []

for n in range(7):
    dados = int(input(f'Digite o {n+1} numero: '))
    if dados % 2 == 0:
        par.append(dados)
    else:
        impar.append(dados)
numeros.append(par[:])
numeros.append(impar[:])
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares foram: {numeros[0]}')
print(f'Os numeros impares foram: {numeros[1]}')
