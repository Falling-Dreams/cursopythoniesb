# -*- coding: UTF-8 -*-
import limpa_dataset
from collections import Counter
import itertools
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
'''
#I) Quantos aplicativos existem?
print("I): " + "Existem", (len(lista_aplicativos)), "aplicativos" + "\n")
'''
#II) Quais são as categorias?
categorias = set([item["Category"] for item in lista_aplicativos])
#print("II): " + "As categorias são:", sorted(categorias), "\n")

#III) Qual a maior avaliação?
app = [app["App"] for app in lista_aplicativos]
#avaliacoes = [avaliacoes["Rating"] for avaliacoes in lista_aplicativos]
#maior_avaliacao = max(avaliacoes)
#maiores_avaliacoes = [i for i, j in enumerate(avaliacoes) if j == maior_avaliacao]
#app_max = list(map(app.__getitem__, maiores_avaliacoes))
#print("A maior avaliação é: ", maior_avaliacao,". " +  "E os aplicativos com essa avaliação são:",sep="")
#print(*sorted(app_max),sep='\n')


#IV) Qual o aplicativo com maior tamanho?
#tamanho_aplicativo = [int(tamanho["Size"]) for tamanho in lista_aplicativos]
#maior_tamanho = max(tamanho_aplicativo)
#maiores_app = [i for i,j in enumerate(tamanho_aplicativo) if j == maior_tamanho]
#app_tamanho = list(map(app.__getitem__, maiores_app))
#print("O maior tamanho de aplicativo é: ", (maior_tamanho//100000), "M" ,". " +  "E os aplicativos com esse tamanho são:",sep="")
#print(*sorted(app_tamanho),sep='\n')

#V) Qual é a categoria com mais aplicativos?
#app_categoria = [(app["App"],app["Category"]) for app in lista_aplicativos]
#qtd_app_categoria = Counter([(y) for (x,y) in app_categoria])
#print("A categoria com mais aplicativos é:", max(qtd_app_categoria, key=qtd_app_categoria.get))

#VI) Qual é a média de avaliação em cada categoria?
#categoria_avaliacao = [(categoria["Category"], float(categoria["Rating"])) for categoria in lista_aplicativos]
#qtd_app_avaliacao = sorted(Counter([(x) for (x,y) in categoria_avaliacao]).items())
#soma = [(k, float(sum([y for (x,y) in categoria_avaliacao if x == k]))) for k in dict(categoria_avaliacao).keys()]
#media_avaliacao = ((x[0], y[1]//x[1]) for x, y in zip(qtd_app_avaliacao, soma))
#print("As médias das avaliações em cada categoria são:" ,*media_avaliacao,sep='\n')

#VII) Daqueles com avaliação maior que 4, qual o conteudo indicativo com mais aplicativos?
#VIII) Qual o desvio padrão da coluna de avaliações?
#IX) Quantos aplicativos foram atualizados em janeiro de 2018?
app_atualizacao = [(atualizacao["App"], atualizacao["Last Updated"]) for atualizacao in lista_aplicativos]

#X) Suponha que você irá utilizar essa planilha em uma solução de IA. Transforme todas as colunas, com exceção do nome do aplicativo, em valores numéricos.