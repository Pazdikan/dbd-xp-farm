import pyautogui
import easyocr
from time import sleep
from PIL import Image

import data
from util.console import log
from rich.text import Text

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

    def click_image(self):
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

    def check_if_banner_present(self):
        try:
            return pyautogui.locateOnScreen('src/assets/banner.png', confidence=0.8) is not None
        except:
            return False
    
    def close_banner(self):
        try:
            pos = pyautogui.locateOnScreen('src/assets/button_ok.png', confidence=0.8)
            pyautogui.click(pos[0] + 10, pos[1] + 10)
        except:
            pass

    def check_if_in_main_menu(self):
        try:
            if pyautogui.locateOnScreen('src/assets/button_play.png', confidence=0.8) is not None:
                return True
        except:
            return False
        
    def enter_killer_lobby(self):
        if not data.ss.check_if_in_main_menu():
            return
        
        pos = pyautogui.locateOnScreen('src/assets/button_play.png', confidence=0.8)
        pyautogui.click(pos[0] + 10, pos[1] + 10)

        sleep(2)

        try:
            pos = pyautogui.locateOnScreen('src/assets/button_play_killer.png', confidence=0.8)
            pyautogui.moveTo(pos[0] + 10, pos[1] + 10, duration=0.25)
            pyautogui.click()

            sleep(10)

            ocr = data.ss.take_and_read_screenshot(data.ss.lobby_button)
            if any("PLAY" in string for string in ocr):
                data.current_state = data.State.INLOBBY
                log(Text("Entered killer lobby!", style="green"))
            else:
                log(Text("Failed to enter killer lobby!", style="red"))
        except:
            log(Text("Failed to enter killer lobby!", style="red"))