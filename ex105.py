dados = {}
def notas(*num, sit=False):
    '''
    Funçao para analizar notas dos alunos
    :param num: notas do aluno
    :param sit: Opçao para ver a situação do aluno
    :return: Retorna o dicionario com as informaçoes do aluno
    '''
    qnt = len(num)
    soma = sum(num)
    dados['Total'] = qnt
    dados['Menor'] = min(num)
    dados['Maior'] = max(num)
    dados['Media'] = soma / qnt
    while sit == True:
        if dados['Media'] <= 5:
            dados['Situação'] = 'A baixo da media'
        elif dados['Media'] <= 7:
            dados['Situação'] = 'Na media'
        else:
            dados['Situação'] = 'Aprovado'
    return dados


resp = notas(5.5,9.5,10,6.5, sit=True)
print(resp)