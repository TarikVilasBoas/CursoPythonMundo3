
def leiaInt(num):
    '''
    testa se a entrada é um numero inteiro
    :param num: entrada do digito
    :return: sucesso caso seja int
    '''
    global n
    while ValueError:
        n =  input('Digite um numero: ').strip()
        try:
            num = int(n)
            return n
        except ValueError:
            print('\033[31mERRO: Digite um numero inteiro valido\033[m')



n = leiaInt('Digite um numero:')
print(f'Voce acabou de digitar o valor {n}')