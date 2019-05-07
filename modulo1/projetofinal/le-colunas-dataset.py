import csv
linhas = []
audiencia = []
with open('googleplaystore_original.csv') as csvDataFile:	
	csvReader = csv.reader(csvDataFile)
	for coluna in csvReader:
		audiencia.append(coluna[8])
		#print((coluna[4]))

print(*set(audiencia),sep='\n')

