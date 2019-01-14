#! python3 
# photoFoldersFinder.py: this program goes through every folder on the hard drive
# and finds photos folders (folders where more than half of the files are photos with 
# width and height more than 500px)

import os
from PIL import Image

min_width = 500
min_height = 500
hard_drive = '/home/shermzlim/' #ubuntu os 

photoFolders = []

for foldername, subfolders, filenames in os.walk(hard_drive):
    totalFiles = len(filenames)
    photoFilesCount = 0 

    # Loop through list of files
    for filename in filenames:
        # if file extension is not .jpg or .png, go to next file 
        if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')):
            continue

        filepath = os.path.join(foldername, filename)
        imageObj = Image.open(filepath)
        width, height = imageObj.size

        # if both width and height is greater than 500px, consider it a photo
        if (width > min_width and height > min_height):
            photoFilesCount += 1 

    # if more than half of total number of files are photos, consider folder a photo folder
    if photoFilesCount > totalFiles/2:
        photoFolders.append(foldername)

print("Your photo folders are:")
for folder in photoFolders:
    print(folder)     