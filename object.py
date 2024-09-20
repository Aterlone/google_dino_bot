import cv2
import numpy as np
from mss import mss
from PIL import Image

sct = mss()

"""

"""

def returnScreen(loc):
    screenshot = sct.grab(loc)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    return screenshot

"""
Show Image
"""
def display(data):
    cv2.imshow("Image", data)

class Object:
    def __init__(self, img_path):
        self.img = cv2.imread(img_path, cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
    def compareScreen(self, screenshot):
        result = cv2.matchTemplate(screenshot, self.img, cv2.TM_CCOEFF_NORMED)
        threshold = 0.60
        yloc, xloc = np.where(result >= threshold)
        if len(xloc > 0):
            return len(xloc)
        return 0