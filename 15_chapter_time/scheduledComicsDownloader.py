#!python3
#This program checks Xkcd website for a new comic every day & downloads it if it is a new comic 
# This program is added to the OS's task scheduler to be ran once everyday 

import requests, bs4, os, shelve

# Creates database for comicNumber (ran once)
# db = shelve.open('xkcdComicNum')
# db['comicNum'] = 2090
# db.close()


# This function downloads Xkcd comics no. x 
def downloadXkcd(x):
    # Downloading page
    url = "https://xkcd.com/{}/".format(x)
    print("Downloading " + url)
    res = requests.get(url)

    # Error handling for when url not valid 
    try: 
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Comic is not updated yet")
        return x

    x = x + 1
    #Selecting comic HTML Element 
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic img')

    # Error handling for retrieving comic Element 
    if comicElem == []:
        print("Could not find comic image.")
    else:
        # Downloading image from imgUrl
        imgUrl = "https:" + comicElem[0].get('src')
        imageRes = requests.get(imgUrl)
        try: 
            res.raise_for_status()
        except requests.exceptions.HTTPError:
            print("Unable to download comic " + imgUrl)
            return x 

        # Writing download to file
        filename = os.path.join("/home/shermzlim/Desktop/atbs_py/15_chapter_time/comicXkcd", os.path.basename(imgUrl))
        imageFile = open(filename, 'wb')
        for chunk in imageRes.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()    
        print("Done")
        return x 

# Retrieving next number of xkcd from database
db = shelve.open('/home/shermzlim/Desktop/atbs_py/15_chapter_time/xkcdComicNum')
x = db['comicNum']

# Running download with the next number of xkcd. If the comic exists,
# increment the number and store it in database. Otherwise, return the same 
# value back to the database
x = downloadXkcd(x)
db['comicNum'] = x
db.close()
 
