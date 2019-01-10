#!python3 
#This program serves as a stopwatch. A lap is made every time the user presses
#ENTER. Ctrl+C to stop the program. The total time, lap numbers and lap time will 
#be printed. Lap timing is immediately copied to clipboard.

import time, pyperclip

# Function calculates & prints the lap number, lap time, and total 
# time after user presses enter.  
def printLapTime():
    lapNow = time.time()
    lapTime = round(lapNow - lastTime, 2)
    totalTime = round(lapNow - startTime, 2)
    
    # Prettifying output:
    lapNumStr = str(lapNum)
    lapTimeStr = str(lapTime)
    totalTimeStr = str(totalTime)
    text = ("Lap #" + lapNumStr.rjust(2) + ": " + totalTimeStr.rjust(5) + " ( " + lapTimeStr.rjust(5) + ")")
    print(text)
    pyperclip.copy(text)
    
    #lapNow is returned so that it can be passed to the next loop
    return lapNow

#Giving user instructions
print("Press Enter to start the stopwatch. Ctrl + C to stop the stopwatch.")

user = input('Press Enter to start:')
startTime = time.time()
print("Started.")
lastTime = startTime
lapNum = 1 

try:
    while True:
        user = input('Press Enter to lap:')
        lastTime = printLapTime()
        lapNum += 1 

except KeyboardInterrupt:
    print("\n")
    printLapTime()
    print("Done.")

