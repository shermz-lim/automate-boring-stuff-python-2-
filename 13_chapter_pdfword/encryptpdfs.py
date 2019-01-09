#!python3 
# ATBS task: write a script that will go through every PDF in a folder 
# (and its subfolders) and encrypt the PDFs using a password provided 
# on the command line. Save each encrypted PDF with an _encrypted.pdf 
# suffix added to the original filename. Before deleting the original 
# file, have the program attempt to read and decrypt the file to ensure 
# that it was encrypted correctly.

import os, PyPDF2, sys 

# Function accepts a pdfFileReader object as an argument and return a 
# pdfWriter object with the contents copied over 
def copyPdf(pdfFileReader):
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdfFileReader.numPages):
        pageObj = pdfFileReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    return pdfWriter         

# Takes in a pdfFileObject, and a password as an argument. #returns false if 
# object is not encrypted, or if password cannot be used to decrypt. returns true otherwise
def checkEncryption(pdfFile, password):
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    if pdfReader.isEncrypted:
        if pdfReader.decrypt(password) == 1:
            return True 
    return False          

# Test command line arguments. Total 3 arguments, 2nd argument should be 
# folder to encrypt, 3rd argument should be the password
try: 
    assert len(sys.argv) == 3 
    assert os.path.isdir(sys.argv[1])
except AssertionError:
    print("Command line arguments are not valid. Try again.")    

folder = sys.argv[1]
password = sys.argv[2]

# Iterating through the folder to retrieve each pdf file 
for folderName, subfolders, filenames in os.walk(folder):
    print("Walking through folder:  " + folderName)
    # Iterating through each file 
    for filename in filenames:
        # Sieving out pdf files 
        if filename.endswith('.pdf'):
            filenamePath = folderName + "/" + filename     

            pdfFileObj = open(filenamePath, 'rb')
            pdfFileReader = PyPDF2.PdfFileReader(pdfFileObj)
            
            # Checks whether pdf file is already encrypted:
            if pdfFileReader.isEncrypted:
                continue 

            print("\nCreating new encrypted file for: " + filename)
            # Return new pdfWriter with copied pdf 
            pdfWriter = copyPdf(pdfFileReader)

            # Adding encryption
            pdfWriter.encrypt(password)

            # Saving the new encrypted file 
            print("Saving new encrypted file in " + folderName)
            outputFilename = filenamePath[:-4] + '_encrypted.pdf'
            outputPdf = open(outputFilename, 'wb')
            pdfWriter.write(outputPdf)
            outputPdf.close()

            # Checking outputPDF's encryption before deleting file:
            print("Checking new encrypted file's encryption")
            outputPdf = open(outputFilename,'rb')
            if checkEncryption(outputPdf, password):
                print("Encryption check successful. Deleting old file...")
                os.remove(filenamePath)
            else: 
                print("Encryption check unsuccessful. Old file not deleted.")    
            print("Task completed.\n")
            outputPdf.close()

    print("\n===============================\n")        



           