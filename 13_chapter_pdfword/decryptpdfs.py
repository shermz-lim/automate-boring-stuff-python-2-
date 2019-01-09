#!python3
#ATBS task: write a program that finds all encrypted PDFs in a
#  folder (and its subfolders) and creates a decrypted copy of 
# the PDF using a provided password. If the password is incorrect, 
# the program should print a message to the user and continue to the next PDF.

import os, PyPDF2, sys 

# Function accepts a pdfFileReader object as an argument and return a 
# pdfWriter object with the contents copied over 
def copyPdf(pdfFileReader):
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdfFileReader.numPages):
        pageObj = pdfFileReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    return pdfWriter         

# Testing command line arguments. 2nd argument - folder. 3rd argument - password for decryption 
try: 
    assert len(sys.argv) == 3 
    assert os.path.isdir(sys.argv[1])
except AssertionError:
    print("Command line arguments are not valid. Try again.")  
    exit()      

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

            # Sieving out encrypted pdf files
            if pdfFileReader.isEncrypted:
                print("\nTrying to decrypt " + filenamePath)
                # Checks whether password is valid 
                if pdfFileReader.decrypt(password) == 1:
                    print("The password is valid. Creating new decrypted file")
                    pdfWriter = copyPdf(pdfFileReader)

                    print("Saving new PDF file")
                    outputPdf = open(filenamePath[:-4] + "_decrypted.pdf", "wb")
                    pdfWriter.write(outputPdf)
                    outputPdf.close()
                    print("Done.")

                else:
                    print("The password you provided does not work.")    
    print("\n=============================\n")                