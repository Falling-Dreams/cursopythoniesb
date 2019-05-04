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
avaliação = [(app["App"],app["Rating"]) for app in lista_aplicativos]
maiores_avaliacoes = list(map(max, *avaliação))
#print(list(map(max, *avaliação)))
#print(*avaliação,sep='\n')
print(maiores_avaliacoes)