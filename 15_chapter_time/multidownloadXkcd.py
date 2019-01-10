# !python3 
# This program contains multipleThread to download Xkcd comics in 
# xkcd folder.
# Why multiple threading? It makes full use of the available 
# broadband's bandwith. Uses Internet connection more efficiently. 

import requests, bs4, threading, os

os.makedirs("comicXkcd", exist_ok=True)

# This function downloads Xkcd comics no. x to no. y. 
def downloadXkcd(x, y):
    for num in range(x, y+1):
        # Downloading page
        url = "https://xkcd.com/{}/".format(num)
        print("Downloading " + url)
        res = requests.get(url)

        # Error handling for when url not valid 
        try: 
            res.raise_for_status()
        except requests.exceptions.HTTPError:
            print("Unable to download " + url)
            continue

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
                continue

            # Writing download to file
            filename = os.path.join("comicXkcd", os.path.basename(imgUrl))
            imageFile = open(filename, 'wb')
            for chunk in imageRes.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()    
            
#Creating & Starting multiple threads
downloadThreads = []
for i in range(1, 1501, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args=[i, i+99])
    downloadThreads.append(downloadThread)
    downloadThread.start()
  
# Preventing next line of code from running until all download is done  
for downloadThread in downloadThreads:
    downloadThread.join()

print("Done!")     