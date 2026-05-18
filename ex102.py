def fatorial(num = 0, show=False):
    """
    Calculo de fatorial
    :param num: O numero a ser fatorado
    :param show: Permite mostrar a conta
    :return: Retorna o valor do fatoramento
    """
    f = 1
    s = ' '
    for c in range(num, 0, -1):
        f *= c
        s += f'{c}'
        if c > 1:
            s += 'x'
    if show:
        print(s, '=', f)
    return f

print(fatorial(5, show=True))
help(fatorial)