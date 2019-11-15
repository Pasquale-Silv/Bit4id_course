import csv

fileCSV = csv.reader('filenamePrimo.csv')        # parametro delimiter=
print(type(fileCSV))

headers = next(fileCSV)
print(headers)

for row in fileCSV:
    print(row)
