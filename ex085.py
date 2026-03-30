num = [[],[]]
valor = 0
for n in range(7):
    valor = int(input(f'Digite o {n+1} numero: '))
    if valor % 2 == 0:
       num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores pares foram: {num[0]}')
print(f'Os numeros impares foram: {num[1]}')
