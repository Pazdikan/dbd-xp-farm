import pyautogui
import easyocr
from time import sleep
from PIL import Image

pyautogui.FAILSAFE = False

reader = easyocr.Reader(['en'])


class Screenshot:
    def __init__(self, sct):
        self.sct = sct


    lobby_button = {
        "top": 927,
        "left": 1580,
        "width": 235,
        "height": 35
    }

    endgame_button = {
        "top": 1000,
        "left": 1650,
        "width": 235,
        "height": 35
    }    

    def click_image():
        try:
            pos = pyautogui.locateOnScreen('screenshot.png', confidence=(0.8))
            if pos != None:
                pyautogui.click(pos[0] + 20, pos[1])
                sleep(0.5)
        except:
            pass

    def take_and_read_screenshot(self, area):
        screenshot = self.sct.grab(area)
        image = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        image.save("screenshot.png")
        return reader.readtext("screenshot.png", detail=0)

    def take_and_read_xp_screenshot(self):
        screenshot = self.sct.grab({
            "top": 700,
            "left": 540,
            "width": 75,
            "height": 35
        })
        image = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        image.save("last_game_xp.png")
        return reader.readtext("last_game_xp.png", detail=0)