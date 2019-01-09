#!python3 
#The program will need to open every file with the .csv extension in the current 
# working directory, read in the contents of the CSV file, and rewrite the contents 
# without the first row to a file of the same name

import os, csv 

# Make new folder to store new csv files 
os.makedirs('headerRemoved', exist_ok=True)

# Iterating through each file in the current working directory 
for filename in os.listdir('.'):
    if not filename.endswith('.csv'):
        continue #skip non csv files 

    print("Removing header from " + filename + '...')    
    csvFile = open(filename)
    csvReader = csv.reader(csvFile)

    outputCsvFile = open(os.path.join('headerRemoved', filename), 'w', newline='')
    csvWriter = csv.writer(outputCsvFile)

    # Iterating through the rows of csvReader & writing it on the Writer
    for row in csvReader:
        # Write row on writer (except for 1st row)
        if csvReader.line_num == 1:
            continue #skip first row 
        csvWriter.writerow(row)

    csvFile.close()
    outputCsvFile.close()    
    print("Done!\n")