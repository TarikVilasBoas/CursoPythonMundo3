#Versao corrigida do professor
'''
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? S/N: '))
    if resp in 'Nn':
        break
print('-'*30)
print(f'Voce digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 NAO faz parte da lista')

'''
# Minha versao

lista = []
while True:
    us = ' '
    num = int(input('Digite um numero: '))
    lista.append(num)
    while us not in 'SN':
        us = str(input('Deseja digitar mais numeros? S/N: ')).upper().strip()[0]
    if us in 'N':
        print(f'Voce digitou {len(lista)} elementos')
        print(f'Em ordem decrescente são: {sorted(lista, reverse=True)}')
        if 5 in lista:
            print('O valor 5 esta na lista.')
        else:
            print('O valor 5 nao foi encontrado;')
        break





