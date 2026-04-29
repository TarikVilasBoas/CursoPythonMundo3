from time import sleep
def maior(*num):
    t = len(num)
    m = max(num)
    print('-'*25)
    print(f'Ao todo foram {t} numeros, {num}')
    print(f'E o maior foi o {m}')


maior(1, 3, 5, 9)
sleep(1)
maior(36,0,15,8,25,)
sleep(1)
maior(8,5,1)
sleep(1)
maior(65, 100, 99, 154, 35, 15, 38)