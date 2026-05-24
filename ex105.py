dados = {}
def notas(*num, sit=False):
    '''
    Funçao para analizar notas dos alunos
    :param num: notas do aluno
    :param sit: Opçao para ver a situação do aluno
    :return: Retorna o dicionario com as informaçoes do aluno
    '''
    dados['Total'] = len(num)
    dados['Menor'] = min(num)
    dados['Maior'] = max(num)
    dados['Media'] = sum(num)/len(num)
    if sit == True:
        if dados['Media'] <= 5:
            dados['Situação'] = 'A baixo da media'
        elif dados['Media'] <= 7:
            dados['Situação'] = 'Na media'
        else:
            dados['Situação'] = 'Aprovado'
    return dados


resp = notas(3.5,4.5,6.8, sit=True)
print(resp)