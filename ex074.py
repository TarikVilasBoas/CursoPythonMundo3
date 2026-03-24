from random import sample

numeros = tuple(sample(range(100),5))
print(numeros)
print(f'O maior numero é {max(numeros)} e o menor é {min(numeros)}')