def ficha(nome, gols ):
    return print(f'O Jogador {nome} marcou {gols} gols')


n = str(input('O nome do Jogador: ')).strip() or "<Desconhecido>"
g = input('Quantos gols ele fez: ').strip()
try:
    gol = int(g)
except ValueError:
    g = 0
ficha(n, g)
