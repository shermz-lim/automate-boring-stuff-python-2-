#!python3 

import csv 

for i in range(1, 10):
    csvFile = open('seed' + str(i) + '.csv', 'w')
    csvWriter = csv.writer(csvFile)
    for x in range(1, 10):
        csvWriter.writerow([y for y in range(1, 10)])
    csvFile.close()    