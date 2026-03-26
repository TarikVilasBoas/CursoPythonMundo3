numeros = []
for n in range(0,5):
    num = int(input('Digite um numero: '))
    if n == 0 or num > numeros[-1]:
        numeros.append(num)
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                break
            pos += 1
print('-' * 30)
print(f'Os valores digitados foram {numeros}')


