import easyocr
from mss import mss
import pyautogui
import win32gui
from time import sleep
from PIL import Image
import numpy as np

reader = easyocr.Reader(['en'])


def level_up():
    pyautogui.mouseDown(x=912, y=759)
    sleep(0.1)
    pyautogui.mouseUp(x=912, y=759)

with mss() as sct:
    while True:
        window = win32gui.GetForegroundWindow()
        window_title = win32gui.GetWindowText(window)
        if "DeadByDaylight" in window_title :
            screenshot = sct.grab({'top': 116, 'left': 784, 'width': 75, 'height': 75})
            image = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
            text = reader.readtext(np.array(image), detail=0)

            if not "50" in text:
                level_up()
            else:
                print("Max level reached!")
            sleep(0.5)
        else:
            print("Script paused, because Dead by Daylight is not focused!")
            sleep(1)
