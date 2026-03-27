lista1 = []
cont1 = cont2 = 0
lista1.append(input('Digite a expressao: '))
iten = lista1[0]
lista2 = list(iten)
print('-'*30)
for p in lista2:
    if p in '(':
        cont1 += 1
    if p in ')':
        cont2 += 1
if cont1 == cont2:
    print('Sua expressao esta correta.')
else:
    print('Sua espressao esta errada.')
