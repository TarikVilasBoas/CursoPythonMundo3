def escreva(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(f'  {txt}')
    print('-' * tam)


escreva('Teste texto')
escreva('Obrigado')
escreva('Fim')