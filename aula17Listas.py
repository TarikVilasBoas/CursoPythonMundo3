num = [1,3,5,7,9]
num[3] = 8    #Troca o valor na posição desejada
num.append(10)   #Adiciona mais um espaço na lista com o valor passado no parametro
num.sort()      #Imprime em ordem
print(num)
num.sort(reverse=True)   #Impime na ordem de tras para fente
num.insert(2, 8)   #Insere o iten na posição escolhida ex=2 e move os demais
num.pop()     #Remove o ultimo valor, se definir a casa nos parametros do pop ela sera excluida
num.remove(8)       #Ira buscar a primeira ocorrencia para eliminar
print(num)
print(f'A lista tem {len(num)} elementos')

print('-'*30)

valores = []
for c in range(0,5):
    valores.append(int(input('Digite um valor: ')))

