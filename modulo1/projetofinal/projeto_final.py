# -*- coding: UTF-8 -*-
"""Projeto Final - Curso Python IESB - Modulo 01

Após avaliar os itens solicitados e o dataset, concluí que a melhor estrutura de dados, neste caso, seria uma lista dos aplicativos 
em que cada índice é um aplicativo, descrito por um dicionário. No qual, as chaves são os atributos do aplicativo e o valor são os dados
de cada aplicativo. Para isso foi preciso modificar o dataset, para que cada atributo fosse separado por uma vírgula, assim, cada valor
fica mapeado a uma chave.
"""

import manipula_dataset
import math

#manipula_dataset.limpar_dataset()
lista_aplicativos = []
chaves = ['App','Category','Rating','Reviews','Size','Installs','Type','Price','Content Rating','Genres','Last Updated','Current Ver',
'Android Ver']
# Retira os espacos em brancos e quebra de linhas, separando os valores a cada virgula, mapeando as chaves a cada valor do aplicativo
with open('googleplaystore.csv', encoding='utf-8') as dataset:
	for linha_csv in dataset:
		valor_app = linha_csv.strip().split(',')	
		aplicativo = {k:v for (k,v) in zip(chaves, valor_app)}
		lista_aplicativos.append(aplicativo)

#'print(*lista_aplicativos,sep='\n')

#I) Quantos aplicativos existem? - OK
#print("I): " + "Existem", (len(lista_aplicativos)), "aplicativos" + "\n")

#II) Quais são as categorias? - OK
categorias = [categoria["Category"] for categoria in lista_aplicativos]
#print("II): " + "As categorias são:", sorted(set(categorias)), "\n")

#III) Qual a maior avaliação? - OK
# maior_avaliacao = max([float(avaliacao["Rating"]) for avaliacao in lista_aplicativos])
# app_avaliacao = {app["App"]: (float(app["Rating"])) for app in lista_aplicativos if float(app["Rating"]) >= maior_avaliacao}
# print("III): " + "A maior avaliação é: ", maior_avaliacao,". " +  "E os aplicativos com essa avaliação são:",sep="")
# print(*sorted(app_avaliacao.keys()),sep='\n')

#IV) Qual o aplicativo com maior tamanho? - OK
# maior_tamanho_app = max([int(tamanho["Size"]) for tamanho in lista_aplicativos])
# app_maior_tamanho = {app_tamanho["App"]: (int(app_tamanho["Size"])) for app_tamanho in lista_aplicativos if int(app_tamanho["Size"])
#  >= maior_tamanho_app}
# print("IV): " + "O maior tamanho de aplicativo é: ", (maior_tamanho_app//1000000), "M" ,". " +  "E os aplicativos com esse tamanho são:",sep="")
# print(*sorted(app_maior_tamanho),sep='\n')

#V) Qual é a categoria com mais aplicativos?
# qtd_app_categoria = dict()
# for categoria in categorias:
#  qtd_app_categoria[categoria] = qtd_app_categoria.get(categoria, 0) + 1
# print("V): " + "A categoria com mais aplicativos é:", max(qtd_app_categoria, key=qtd_app_categoria.get), "\n")
# print(qtd_app_categoria)
# qtd_app_categoria.get(categoria, 0)}


#VI) Qual é a média de avaliação em cada categoria?
#categoria_avaliacao = [[categoria["Category"], (float(categoria["Rating"]))] for categoria in lista_aplicativos]
#avaliacao_soma = dict()
#qtd_avaliacao = dict()
#avaliacao_soma = {categoria: (avaliacao_soma.get(categoria, 0) + avaliacao) for categoria, avaliacao in categoria_avaliacao}
#qtd_avaliacao = {categoria: (qtd_avaliacao.get(categoria, 0) + 1) for categoria,avaliacao in categoria_avaliacao if avaliacao != 0}
#media_avaliacao = [i/j for (i,j) in zip(avaliacao_soma.values(), qtd_avaliacao.values())]
#media_avaliacao_categoria = list(zip(qtd_avaliacao.keys(),media_avaliacao))
#print("VI): A média de avaliação em cada categoria é:")
#print(*media_avaliacao_categoria,sep='\n')

#VII) Daqueles com avaliação maior que 4, qual o conteudo indicativo com mais aplicativos?
#app_audiencia = [audiencia["Content Rating"] for audiencia in lista_aplicativos if float(audiencia["Rating"]) >= 4]
#qtd_app_audiencia = dict()
#qtd_app_audiencia = {audiencia: (qtd_app_audiencia.get(audiencia, 0) + 1) for audiencia in app_audiencia}
#print("VII): " + "O conteudo indicativo com mais aplicativos é:", max(qtd_app_audiencia, key=qtd_app_audiencia.get), "\n")

#VIII) Qual o desvio padrão da coluna de avaliações?
#avaliacao = [float(avaliacao["Rating"]) for avaliacao in lista_aplicativos if float(avaliacao["Rating"]) > 0]
#media = (sum(avaliacao))/len(avaliacao)
#passo2 = [(n - media)**2 for n in avaliacao]
#desvio_padrao = math.sqrt((sum(passo2))/len(avaliacao))
#print("VIII): O desvio padrão é:", desvio_padrao)

#IX) Quantos aplicativos foram atualizados em janeiro de 2018?
#app_atualizacao = [(atualizacao["App"], str(atualizacao["Last Updated"])) for atualizacao in lista_aplicativos]
#atualizacao = [(x,y) for (x,y) in app_atualizacao if ("January") in y and ("2018") in y]
#print("IX): " + "Foram atualizados", len(set(atualizacao)), "aplicativos")

#X) Suponha que você irá utilizar essa planilha em uma solução de IA. Transforme todas as colunas, com exceção do nome
#do aplicativo, em valores numéricos.
