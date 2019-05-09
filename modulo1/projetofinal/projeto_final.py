# -*- coding: UTF-8 -*-
import limpa_dataset
import math
limpa_dataset.manipula_dataset()
lista_aplicativos = []
lista_temp = []
cabecalho = ['App','Category','Rating','Reviews','Size','Installs','Type','Price','Content Rating','Genres','Last Updated',
			'Current Ver','Android Ver']
with open('googleplaystore.csv', encoding='utf-8') as arquivo:
	for linha in arquivo:
		line = linha.strip().split(',') #retira os espacos em brancos e quebra de linhas, separando os valores a cada virgula	
		aplicativo = {k:v for (k, v) in zip(cabecalho, line)}
		lista_aplicativos.append(aplicativo)

#print(*lista_aplicativos,sep='\n')
'''
#I) Quantos aplicativos existem?
print("I): " + "Existem", (len(lista_aplicativos)), "aplicativos" + "\n")

#II) Quais são as categorias?
categorias = [categoria["Category"] for categoria in lista_aplicativos]
print("II): " + "As categorias são:", sorted(set(categorias)), "\n")

#III) Qual a maior avaliação?
app = [app["App"] for app in lista_aplicativos]
avaliacoes = [avaliacoes["Rating"] for avaliacoes in lista_aplicativos]
maior_avaliacao = max(avaliacoes)
maiores_avaliacoes = [i for i, j in enumerate(avaliacoes) if j == maior_avaliacao]
app_max = list(map(app.__getitem__, maiores_avaliacoes))
print("III): " + "A maior avaliação é: ", maior_avaliacao,". " +  "E os aplicativos com essa avaliação são:",sep="")
print(*sorted(app_max),sep=',')
print('\n')

#IV) Qual o aplicativo com maior tamanho?
tamanho_aplicativo = [int(tamanho["Size"]) for tamanho in lista_aplicativos]
aplicativo_tamanho = {k:v for (k, v) in zip(app, tamanho_aplicativo)}
maior_tamanho = max(aplicativo_tamanho.values())
maiores_app = [i for i,j in enumerate(tamanho_aplicativo) if j == maior_tamanho]
app_tamanho = list(map(app.__getitem__, maiores_app))
print("IV): " + "O maior tamanho de aplicativo é: ", (maior_tamanho//1000000), "M" ,". " +  "E os aplicativos com esse tamanho são:",sep="")
print(*sorted(set(app_tamanho)),sep=',')
print('\n')

#V) Qual é a categoria com mais aplicativos?
qtd_app_categoria = dict()
for categoria in categorias:
  qtd_app_categoria[categoria] = qtd_app_categoria.get(categoria, 0) + 1
print("V): " + "A categoria com mais aplicativos é:", max(qtd_app_categoria, key=qtd_app_categoria.get), "\n")

#VI) Qual é a média de avaliação em cada categoria?
categoria_avaliacao = [[categoria["Category"], (float(categoria["Rating"]))] for categoria in lista_aplicativos]
avaliacao_soma = dict()
for categoria,avaliacao in categoria_avaliacao:
	avaliacao_soma[categoria] = avaliacao_soma.get(categoria, 0) + avaliacao
qtd_avaliacao = dict()
for categoria,avaliacao in categoria_avaliacao:
	if avaliacao != 0 :
		qtd_avaliacao[categoria] = qtd_avaliacao.get(categoria, 0) + 1
media_avaliacao = [i/j for (i,j) in zip(avaliacao_soma.values(), qtd_avaliacao.values())]
media_avaliacao_categoria = list(zip(qtd_avaliacao.keys(),media_avaliacao))
print("VI): A média de avaliação em cada categoria é:")
print(*media_avaliacao_categoria,sep='\n')

#VII) Daqueles com avaliação maior que 4, qual o conteudo indicativo com mais aplicativos?
app_audiencia = [audiencia["Content Rating"] for audiencia in lista_aplicativos if float(audiencia["Rating"]) >= 4]
qtd_app_audiencia = dict()
for audiencia in app_audiencia:
  qtd_app_audiencia[audiencia] = qtd_app_audiencia.get(audiencia, 0) + 1
print("VII): " + "O conteudo indicativo com mais aplicativos é:", max(qtd_app_audiencia, key=qtd_app_audiencia.get), "\n")
'''
#VIII) Qual o desvio padrão da coluna de avaliações?
avaliacao = [float(avaliacao["Rating"]) for avaliacao in lista_aplicativos if float(avaliacao["Rating"]) > 0]
media = (sum(avaliacao))/len(avaliacao)
passo2 = [(n - media)**2 for n in avaliacao]
desvio_padrao = math.sqrt((sum(passo2))/len(avaliacao))
print("VIII): O desvio padrão é:" ,desvio_padrao)

#IX) Quantos aplicativos foram atualizados em janeiro de 2018?
#app_atualizacao = [(atualizacao["App"], str(atualizacao["Last Updated"])) for atualizacao in lista_aplicativos]
#atualizacao = [(x,y) for (x,y) in app_atualizacao if ("January") in y and ("2018") in y]
#print("IX): " + "Foram atualizados", len(set(atualizacao)), "aplicativos")

#X) Suponha que você irá utilizar essa planilha em uma solução de IA. Transforme todas as colunas, com exceção do nome do aplicativo, em valores numéricos.
