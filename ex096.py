def area(l, c):
    t = l * c
    print(f'A área de um terreno de {l} * {c} é de: {t}')


print('Controle de terrenos')
print('-'*25)
a = float(input('Largura do terreno (m): '))
b = float(input('Comprimento do terreno (m): '))

area(a,b)
