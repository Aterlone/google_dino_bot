import cv2
import pyautogui
import time
import math

import object

loc = {
    "left": 500,    # X coordinate of the top-left corner
    "top": 280,     # Y coordinate of the top-left corner
    "width": 120,   # Width of the screenshot
    "height": 120 
}


display = object.display
cacti = []
bird = object.Object("images/obstacles/4.png")
for i in (0,1):
    cacti.append(object.Object(f"images/obstacles/{i}.png"))
while 1:
    times = 0
    time_n = time.time()
    screen = object.returnScreen(loc)
    print(1/(time.time() - time_n))
    loc["width"] += (time.time()-time_n)*5
    for o in cacti:
        if o.compareScreen(screen):
            pyautogui.press("space")
    if bird.compareScreen(screen):
        display(screen)
    cv2.waitKey(100)
