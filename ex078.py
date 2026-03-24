num = []
for v in range(5):
    num.append(int(input(f'Digite o numero da posição {v}: ')))
print('_-'*40)
print(f'Voce digitou os valores {num}')
print(f'O maior valor entre eles é {max(num)} e esta nas posiçoes: ',end='')
for p, n in enumerate(num):
    if n == max(num):
        print(f'{p}, ',end='')
print(f'\nO menor valor é o {min(num)} que esta nas posiçoes: ', end='')
for p, n in enumerate(num):
    if n == min(num):
        print(f'{p}, ',end='')

