from datetime import datetime
funcionario = {}
funcionario['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
funcionario['idade'] = datetime.now().year - ano
ctps = int(input('N carteira de trabalho (0 nao tem): '))
if ctps != 0:
    funcionario['contratacao'] = int(input('Ano de contratação: '))
    funcionario['salario'] = float(input('Salario: '))
    aposent = funcionario['contratacao'] - ano + 35
    funcionario['aposentadoria'] = aposent
for i, v in funcionario.items():
    print(f'O {i} é = {v}')