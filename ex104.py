
def leiaInt(num):
    global n
    while ValueError:
        n =  input('Digite um numero: ').strip()
        try:
            num = int(n)
            return n
        except ValueError:
            print('\33[31mERRO: Digite um numero inteiro valido\33[m')



n = leiaInt('Digite um numero:')
print(f'Voce acabou de digitar o valor {n}')