## Praticando 3

lista = ["Python", 1, 0.5, "C", "Java", "Go", 5, 6, -9, 260, "JS", "Kotlin"]

# mostre na tela CADA elemento da lista
for elemento in lista:
    print(elemento)
print()

# quantos elementos existem na lista?
cont = 0
for elemento in lista:
    cont += 1

print(len(lista), '\n')

# mostre apenas os números da lista
for elemento in lista:
    if float != type(elemento) != int:
        continue

    print(elemento)