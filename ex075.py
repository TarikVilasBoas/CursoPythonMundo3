a = int(input('Digite um numero: '))
b = int(input('Digite mais um numero: '))
c = int(input('Mais um :'))
d = int(input('O ultimo: '))
numeros = (a,b,c,d)
print(f'Voce digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} veses')
if 3 in numeros:
    print(f'O valor 3 esta na {numeros.index(3)} posição')
print('Numeros pares:')
for p in numeros:
    if p % 2 == 0:
        print(p)
