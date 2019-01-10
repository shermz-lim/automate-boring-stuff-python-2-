#!python3 
#this program counts down from 60 and play an alarm once it is done 

import subprocess, time

for i in range(60, 0, -1):
    print(i)
    time.sleep(1)

print("!!!!!!!! 0 !!!!!!!!!")
subprocess.Popen(['/usr/bin/rhythmbox', 'alarm.wav'])