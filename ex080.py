numeros = []
for n in range(1):
    num = int(input('Digite um numero: '))
    if not numeros:
        numeros.append(num)
        print(f'Iten adicionado na posição {n}')
    if num > numeros[0]:
        numeros.insert(1,num)
    elif num < numeros[0]:
        numeros.insert(0, num)