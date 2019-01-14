#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

square_fit_size = 300
logo_filename = 'catlogo.png'

logoIm = Image.open(logo_filename)
logoIm = logoIm.resize((50, 45))
logoWidth, logoHeight = logoIm.size

# Makes dir to store new images
os.makedirs('withLogo', exist_ok=True)

# Loop over all files in the working directory.
for filename in os.listdir('.'):
    # skip non-image files and the logo file itself 
    if not (filename.endswith('.jpg') or filename.endswith('.png')) or filename == logo_filename:
        continue 
    
    im = Image.open(filename)
    width, height = im.size 

    # Checks if image needs to be resized:
    if width > square_fit_size or height > square_fit_size:
        if width > height:
            height = int((square_fit_size/width) * height)
            width = square_fit_size
        else:
            width = int((square_fit_size/height) * width)
            height = square_fit_size

        # Resize the image 
        print("Resizing {}...".format(filename))
        im = im.resize((width, height))
                            
    #Calculating the pasting position for logo 
    pasteX = width - logoWidth
    pasteY = height - logoHeight
    print("Adding logo to {}...".format(filename))
    im.paste(logoIm, (pasteX, pasteY), logoIm)        

    # Saving file 
    im.save(os.path.join('withLogo', filename))

