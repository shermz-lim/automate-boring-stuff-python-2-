#!python3 
# a program that will decrypt the PDF by trying every possible English word 
# until it finds one that works. Pass in encrypted pdf in the command line:

import PyPDF2, sys, os, random

# Testing command line argument:
try:
    assert len(sys.argv) == 2 
    assert os.path.exists(sys.argv[1])
    filename = sys.argv[1]
    assert filename.endswith('.pdf')
    fileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(fileObj)
    assert pdfReader.isEncrypted
except AssertionError:
    print("Command line argument is not valid. Please provide an encrypted pdf file")
    exit()

# Dictionary.txt is the textfile containing 44000 english words
# Creating words list with both lower % uppercase english words 
words = []
dicFileObj = open('dictionary.txt', 'r')
for word in dicFileObj.readlines():
    # Removes the newline 
    words.append(word[:-1])
    words.append(word[:-1].lower())
dicFileObj.close()    
random.shuffle(words)


print("Starting attempt to decrypt PDF " + filename)
password = ''
for word in words:
    # If password works, breaks out of loop
    if pdfReader.decrypt(word) == 1:
        password = word
        break 

# Printing password if found
if password:
    print("The password is " + password)
else:
    print("The password cannot be found.")    

