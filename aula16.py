#Tuplas em python

food = ('Arroz', 'Feijao', 'Amendoim', 'Carne')  #Iniciando uma tupla, que sempre será imutavel
print(food[1]) # Acesso a posição por []
print(food[1:3]) # Fatiamento vai imprimir do 1 ao 2
print(sorted(food))
print('-'*30)
for comida in range(0,len(food)):
    print(food[comida], comida)
print('-'*30)
for pos, comida in enumerate(food): # A funçao enumerate tras a posição e o produto
    print(pos, comida)
print('-'*30)
for comida in food:
    print(sorted(comida))  # Ordena os nomes
print('-'*30)
a = (1, 8, 2, 3)
b = (6, 8, 4, 7, 5)
c = a + b
print(sorted(c))
print(c.count(8))   #Conta quantas vezes o iten aparece
print(c)
print(c.index(8, 2))    #Pega a posição do iten, começando a procura da segunda casa(Deslocamento)

pessoa = ('Tarik', '30', 'M', '1.72cm') #Aceita varios tipos de dados na mesma tupla
print(pessoa)