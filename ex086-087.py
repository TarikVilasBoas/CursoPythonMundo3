matriz = []
par = soma2 = 0
for n in range(3):
    iten = []
    for i in range(3):
        dados = int(input(f'Digite o numero [{n},{i}]: '))
        iten.append(dados)
        if dados % 2 == 0:
            par += dados
        if i == 2:
            soma2 += dados
    matriz.append(iten)
print('-='*30)
for l in range(3):
    for c in range(3):
        print(f'( {matriz[l][c]:^5} )',end=' ')
    print()
print('-='*30)
print(f'A soma de todos os pares é {par}')
print(f'A soma da terceira coluna é {soma2}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')