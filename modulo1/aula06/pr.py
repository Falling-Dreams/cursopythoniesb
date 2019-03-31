#usando list comprehensions crie uma lista com o quadrado dos numeros 
#digitados pelo usuario e mostre todos eles separados por '@'. Exemplo: "1 @ 
#4 @9"

lista = [int(i)**2 for i in input().split()]
print("O quadrado e: ", lista, sep=" @ ")
#lista = [str(int(i)**2) for i in input().split()]
#print(' @ '.join(lista))