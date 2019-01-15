#! python3 
# This program nudges the mouse every 10 seconds 

import pyautogui, time

print("This program nudges your mouse every 10 seconds. Press Ctrl-C to quit.")

try: 
    while True:
        time.sleep(10)
        pyautogui.moveRel(1, 0)
        pyautogui.moveRel(-1, 0)

except KeyboardInterrupt:
    print("Program terminated.")        