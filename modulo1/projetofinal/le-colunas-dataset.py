import csv
linhas = []
avaliacao = []
with open('googleplaystore.csv') as csvDataFile:	
	csvReader = csv.reader(csvDataFile)
	for coluna in csvReader:
		avaliacao.append(coluna[2])
		#print((coluna[2]))

print(len(avaliacao))		
#print(*linhas,sep='\n')
		