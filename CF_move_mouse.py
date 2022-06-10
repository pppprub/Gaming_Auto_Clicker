# py -m pip install pyautogui #install pyautogui package in cmd
import pyautogui
import time
import sys
from datetime import datetime
import random
# run the python IDLE as administrator, and then open and run this script in the IDLE 
numMin = 80 #time of animation running
pyautogui.moveTo(1580, 780)#position of joinning game button
sleeptime=20 #sleep time in sec
x=0
print("press CTRL + C to exit")
# pyautogui.size() screen size: 1920 X 1080
try:
    while(x<numMin):
        time.sleep(round(0.5*sleeptime))
        x+=sleeptime/60
        pyautogui.moveTo(1580, 780)#position of joinning game button
        pyautogui.click()
        pyautogui.press("ctrl")
        pyautogui.press("W")
        pyautogui.scroll(2) 
        time.sleep(round(0.5*sleeptime))
        pyautogui.moveTo(random.randint(300, 1200), random.randint(300, 700))#position of joinning game button
        pyautogui.press("shift")
        pyautogui.press("shift")
        pyautogui.press("ctrl")
        print("Animation time left {} mins".format(numMin-x))
except KeyboardInterrupt:
    print('\n')