import pyautogui
import random
import time


x,y = pyautogui.size()
type(x)
while True:
    new_x = random.randrange(x)
    new_y = random.randrange(y)
    timer_time = random.randrange(2,6)
    pyautogui.moveTo(new_x,new_y,timer_time)
    
