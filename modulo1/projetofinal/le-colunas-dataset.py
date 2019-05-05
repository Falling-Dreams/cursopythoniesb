import csv
linhas = []
atualizacao = []
with open('googleplaystore.csv') as csvDataFile:	
	csvReader = csv.reader(csvDataFile)
	for coluna in csvReader:
		atualizacao.append(coluna[10])
		#print((coluna[4]))

print(*atualizacao,sep='\n')
#print(tamanho[10472])
