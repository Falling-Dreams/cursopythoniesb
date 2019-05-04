# -*- coding: UTF-8 -*-
import limpa_dataset
limpa_dataset.manipula_dataset()
lista_aplicativos = []
lista_temp = []
cabecalho = ['App','Category','Rating','Reviews','Size','Installs','Type','Price','Content Rating','Genres','Last Updated','Current Ver','Android Ver']
with open('googleplaystore.csv', encoding='utf-8') as arquivo:
	for linha in arquivo:
		line = linha.strip().split(',') #retira os espacos em brancos e quebra de linhas, separando os valores a cada virgula	
		aplicativo = {k:v for (k, v) in zip(cabecalho, line)}
		lista_aplicativos.append(aplicativo)

#print(*lista_aplicativos,sep='\n')
#I) Quantos aplicativos existem?
#print("I): " + "Existem", (len(lista_aplicativos)), "aplicativos" + "\n")

#II) Quais são as categorias?
#categorias = set([item["Category"] for item in lista_aplicativos])
#print("II): " + "As categorias são:", sorted(categorias), "\n")

#III) Qual a maior avaliação?
#app_avaliacoes = []
app = [app["App"] for app in lista_aplicativos]
avaliacoes = [avaliacoes["Rating"] for avaliacoes in lista_aplicativos]
maior_avaliacao = max(avaliacoes)
maiores_avaliacoes = [i for i, j in enumerate(avaliacoes) if j == maior_avaliacao]
app_max = list(map(app.__getitem__, maiores_avaliacoes))
print("A maior avaliação é: ", maior_avaliacao,". " +  "E os aplicativos com essa avaliação são:",sep="")
print(*sorted(app_max),sep='\n')

