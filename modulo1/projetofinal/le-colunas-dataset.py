import csv

current_version = []
with open('googleplaystore.csv') as csvDataFile:	
	csvReader = csv.reader(csvDataFile)
	for coluna in csvReader:
		current_version.append(coluna[1])

print((current_version))


