from time import sleep
resp = ' '
fverde = '\33[42m'
fvermelho = '\33[41m'
fazul = '\33[44m'
reset = '\033[0m'

def intro():
    print(f'{fvermelho}~'*25)
    print(f'{'SISTEMA DE AJUDA PYHELP':^25}')
    print('~'*25)
    print(reset)
def ajuda(txt):
    '''
    Mostra as informações sobre funções e bibliotecas
    :param txt: função / biblioteca
    :return: info
    '''
    frase = f'ACESSANDO O MANUAL DO: {txt}'
    t = len(frase)
    print(f'{fazul}-'*t)
    print(frase)
    print('-'*t)
    sleep(0.5)
    print(fverde)
    help(txt)
    print(reset)



while resp not in 'fim':
    intro()
    resp = str(input('Função ou Biblioteca > ')).lower()
    if resp == 'fim':
        break
    ajuda(resp)