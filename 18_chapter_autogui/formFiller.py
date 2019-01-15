#! python3 
# Fills out google form with pyautogui 

import pyautogui, time

nameField = (860, 560)
submitAnother = (800, 440)

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of the room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Uphold the law.'},
           ]

pyautogui.PAUSE = 0.5

for person in formData:
    print("You have 5 seconds to kill the script by pressing Ctrl-C")
    time.sleep(5)

    print("Entering {}'s info...".format(person['name']))
    pyautogui.click(nameField[0], nameField[1])

    # Fill out the name field 
    pyautogui.typewrite(person['name'] + '\t')

    # Fill out the fear field 
    pyautogui.typewrite(person['fear'] + '\t')

    # Fill out the wizard field 
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', 'enter', '\t'], interval=0.5)
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', 'enter', '\t'], interval=0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', 'enter', '\t'], interval=0.5)
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', 'enter', '\t'], interval=0.5)

    # Fill out robocop field 
    if person['robocop'] == 1:
        pyautogui.typewrite(['space', '\t'], interval=0.5)
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'], interval=0.5)
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'], interval=0.5)
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'], interval=0.5)
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'], interval=0.5)

    # Fill out additional comments field 
    pyautogui.typewrite(person['comments'] + '\t')

    #Clicking submit button 
    pyautogui.press('enter')    
    print("Clicked submit.")

    # Waiting for response to load 
    time.sleep(5)

    #Click submit another response
    pyautogui.click(submitAnother[0], submitAnother[1])