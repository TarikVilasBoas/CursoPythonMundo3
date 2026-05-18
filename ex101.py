from datetime import date

def voto(ano):
    idade = date.today().year - ano
    if idade < 18:
        return f'Com {idade} anos nao é obrigado a votar'
    elif idade >= 18 and idade <= 65 :
        return f'Com {idade} voce é obrigado a votar'
    else:
        return f'Com {idade} Seu voto é opcional'


nasc = int(input('Em que ano voce nasceu? '))
print(voto(nasc))
