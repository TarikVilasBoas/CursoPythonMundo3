from time import sleep
def contador(a, b, c):
    valor = []
    if a < b:
        print('-'* 40)
        print(f'{a}',end=', ')
        while a <= b:
            a += c
            valor.append(str(a))
        print(f'{', '.join(valor)}')
        print('-'*40)
    elif a > b:
        print('-'*40)
        print(f'{a}',end=', ')
        while a >= b:
            a += c
            valor.append(str(a))
        print(f'{', '. join(valor)}')
        print('-'*40)


contador(1, 10, 1)
contador(10, 1, -2)
print('Sua vez de definir os parametros da contagem.')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)

