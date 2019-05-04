# -*- coding: UTF-8 -*-

#1: limpar o dataset (retirando a virgula dos campos installs e last_updated)
	#observar o padrao das aspas
#2: encontrar uma solucao que mapeia cabecalho com lista formada com split em \n

#zip creates a new list, filled with tuples containing elements from the iterable arguments			
#dictionary comprehension
#new_dict = {k: v for k, v in zip(keys, values)}
#aplicativo = dict(zip(cabecalho, line))

lista_aplicativos = []
lista_temp = []
cabecalho = ['App','Category','Rating','Reviews','Size','Installs','Type','Price','Content Rating','Genres','Last Updated','Current Ver','Android Ver']
#conjunto = set(cabecalho)
#print(conjunto)
with open('googleplaystore.csv', encoding='utf-8') as arquivo:
	for linha in arquivo:
		line = linha.strip().split(',') #retira os espacos em brancos e quebra de linhas, separando os valores a cada virgula	
		aplicativo = {k:v for (k, v) in zip(cabecalho, line)}
		lista_aplicativos.append(aplicativo)
		
print(*lista_aplicativos,sep='\n')

