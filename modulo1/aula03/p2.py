## Praticando 2

lista = ["João", 18, "Python", "Maria", 20, "C"]

# adicione Douglas, 20 e Java na lista
## lista.append("Douglas")
## lista.append(20)
## lista.append("Java")
lista.extend(["Douglas", 20, "Java"])

# troque a idade de joão para 25
lista[1] = 25

# mostre a quantidade de 20 na lista
print(lista.count(20))

# remova Java da lista
lista.pop()
## del lista[-1]
## del lista[8]