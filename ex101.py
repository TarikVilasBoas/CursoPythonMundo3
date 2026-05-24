
def voto(ano):
    from datetime import date        # A biblioteca pode ser chamada dentro da funçao e ira funcionar so nela
    # Isso ajuda na reduçao do espaço usado na memoria
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos nao é obrigado a votar'
    elif idade > 16 and idade <= 65 :
        return f'Com {idade} voce é obrigado a votar'
    else:
        return f'Com {idade} Seu voto é opcional'

nasc = int(input('Em que ano voce nasceu? '))
print(voto(nasc))
