#!python3
#This program loops through the excel files in the current working directory and convert 
#all of them into CSV files & store them in csvFolder 

import os, openpyxl, csv 

# Making folder to store csv files
os.makedirs("csvFolder", exist_ok=True)

# Looping through each file in current working directory 
for filename in os.listdir('.'):
    # Ignores the non-xlsx files 
    if not filename.endswith('xlsx'):
        continue 
    
    wb = openpyxl.load_workbook(filename)

    print("Converting workbook: " + filename)
    # Iterating through each sheet of workbook
    for sheet in wb.get_sheet_names():
        ws = wb.get_sheet_by_name(sheet)

        # Creating CSV writer 
        csvFilename = filename[:-5] + "_" + sheet + ".csv"
        csvFile = open(os.path.join("csvFolder/", csvFilename), 'w')
        csvWriter = csv.writer(csvFile)

        # Iterating through each row of sheet
        for row in ws.iter_rows():
            rowValues = []
            # Appending each cell of row to a list
            for cell in row:
                rowValues.append(cell.value)
            # Writing list to csvWriter     
            csvWriter.writerow(rowValues)    
            
    csvFile.close()
    print("Done conversion. \n")