alunos = []
while True:
    resp = ' '
    nome = str(input('Nome: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media =( nota1 + nota2 ) / 2
    alunos.append([nome, [nota1, nota2], media])
    while resp not in 'SsNn':
        resp = str(input('Deseja registrar mais? S/n: '))
    if resp in 'Nn':
        break
print('-='*40)
print(f'{'N':<4} {'NOME':<10} {'MÉDIA':>8}')
print('-'*40)
for i, a in enumerate(alunos):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8}')
print('-'*40)
while True:
    al = int(input('Deseja ver a nota de qual aluno? (999 parar): '))
    if al == 999:
        print('Finalizado')
        break
    if al <= len(alunos) - 1:
        print(f'As notas de {alunos[al][0]} sao {alunos[al][1]}')
