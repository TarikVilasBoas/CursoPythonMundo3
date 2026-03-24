mercearia = ('Pao de Queijo',13.90,'Arroz',28.90,'Farofa',8.50,'Bacon',12.99)
print('='*40)
print(f'{"Mercado do so Ze":^40}')
print('='*40)
for pos in range(0,len(mercearia)):
    if pos % 2 == 0:
        print(mercearia[pos].ljust(30,'-'), 'R$',end='')
    else:
        print(f'{mercearia[pos]:>6.2f}')