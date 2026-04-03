aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media de {aluno['Nome']}: '))
for n, m in aluno.items():
    print(f'O {n} é {m}')
print('A situação é : ',end='')
if aluno['Media'] >= 6:
    print('Aprovado')
else:
    print('Reprovado')