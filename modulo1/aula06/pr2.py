#usando list comprehensions pegues os numeros de 10 ate 100 e troque por '-'
#todos os numeros impares. Exemplo: [10,'-',12,'-']

lista = [i for i in range(10, 101) if i % 2 == 0]
#falta trocar impar por '-'

print(lista)