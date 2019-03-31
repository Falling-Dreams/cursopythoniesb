## Praticando 4

lista = []

# preencha a lista até que seja digitado o valor -1 e
# mostre CADA elemento no FINAL
while True:
    n = input()

    if n == '-1':
        break

    lista.append(n)

for n in lista:
    print(n)

print(max(lista))