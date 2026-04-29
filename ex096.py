def area(l, c):
    t = l * c
    print(f'A área de um terreno de {l} * {c} é de: {t}m2')

#Programa principal
print('Controle de terrenos')
print('-'*25)
l = float(input('Largura do terreno (m): '))
c = float(input('Comprimento do terreno (m): '))

area(l,c)
