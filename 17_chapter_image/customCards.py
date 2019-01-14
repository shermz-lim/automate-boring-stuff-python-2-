#! python3 
# program creates a custom card for every guests in guests.txt 

from PIL import Image, ImageDraw, ImageFont
import os 

# Obtaining guests list 
guestsFile = open('guests.txt')
guests = guestsFile.read().split("\n")
guestsFile.close()   

fontsFolder = "/usr/share/fonts/truetype/open-sans/"
imageFont = ImageFont.truetype(os.path.join(fontsFolder, 'OpenSans-BoldItalic.ttf'), 32)

# Obtaining cat logo & resizing it 
catIm = Image.open('catlogo.png')
catWidth, catHeight = catIm.size 
catIm = catIm.resize((48, int(48/catWidth * catHeight)))
catWidth, catHeight = catIm.size 

# Iterate through guess list 
for guest in guests:
    # Create new card 
    cardIm = Image.new('RGBA', (288, 360), (255, 255, 255, 255))

    # Decorate cardIm with catIm 
    for width in range(0, 288, catWidth):
        for height in [0, 360 - catHeight]:
            cardIm.paste(catIm, (width, height), catIm)

    # Drawing outline for card
    drawObj = ImageDraw.Draw(cardIm)
    drawObj.line([(0, 0), (287, 0), (287, 359), (0, 359), (0, 0)], (0, 0, 0, 255))

    # Writing text on card
    textwidth, textheight = drawObj.textsize(guest, font=imageFont)
    drawObj.text(((288 - textwidth)/2, (360 - textheight)/2), guest, (0, 0, 0), font=imageFont)

    # Saving image 
    cardIm.save('{}_card.png'.format(guest))
    print("Made card for {}".format(guest))

