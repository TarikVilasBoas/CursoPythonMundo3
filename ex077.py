palavras = ('Abacaxi','Cenoura','Telefone','Otimo')

for iten in palavras:
    print(f'\nA palavra {iten.upper()} tem as vogais ',end=' ')
    for letra in iten:
        if letra.lower() in 'aeiou':
            print(letra,end='')