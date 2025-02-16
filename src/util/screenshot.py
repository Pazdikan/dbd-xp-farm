import pyautogui
import easyocr
from time import sleep
from PIL import Image
import numpy as np

import data
from util.console import log
from rich.text import Text
import os

pyautogui.FAILSAFE = False

reader = easyocr.Reader(["en"])


class Screenshot:
    def __init__(self, sct):
        self.sct = sct

    lobby_button = {"top": 927, "left": 1580, "width": 235, "height": 35}

    endgame_button = {"top": 1000, "left": 1650, "width": 235, "height": 35}

    def click_image(self, path):
        if not os.path.exists(path):
            return

        try:
            pos = pyautogui.locateOnScreen(path, confidence=(0.8))
            if pos != None:
                pyautogui.moveTo(pos[0] + 20, pos[1] + 20, duration=0.25)
                pyautogui.mouseDown(button="left")
                sleep(0.05)
                pyautogui.mouseUp(button="left")
                sleep(0.5)
        except:
            pass

    def take_and_read_screenshot(self, area):
        screenshot = self.sct.grab(area)
        image = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        return reader.readtext(np.array(image), detail=0)

    def take_and_read_xp_screenshot(self):
        screenshot = self.sct.grab({"top": 700, "left": 540, "width": 75, "height": 35})
        image = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        return reader.readtext(np.array(image), detail=0)

    def take_and_read_bloodpoint_screenshot(self):
        screenshot = self.sct.grab(
            {"top": 487, "left": 110, "width": 300, "height": 50}
        )
        image = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        return reader.readtext(np.array(image), detail=0)

    def take_and_read_iri_shards_screenshot(self):
        screenshot = self.sct.grab(
            {"top": 43, "left": 1500, "width": 120, "height": 30}
        )
        image = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        shards = reader.readtext(np.array(image), detail=0)

        if len(shards) > 0:
            try:
                return int(shards[0].replace(" ", ""))
            except:
                return 0

        return 0

    def take_and_read_actions_screenshot(self):
        screenshot = self.sct.grab(
            {"top": 898, "left": 656, "width": 800, "height": 50}
        )
        image = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        return reader.readtext(np.array(image), detail=0)

    def take_and_read_blight_rush_number_screenshot(self):
        screenshot = self.sct.grab({"top": 892, "left": 177, "width": 25, "height": 35})
        image = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        return reader.readtext(np.array(image), detail=0)

    def take_and_read_killer_name_screenshot(self):
        if data.config.get("killer_detection", section="general") == "0":
            log(Text(f"Automatic killer detection is turned off", style="blue"))
            log(
                Text(
                    f"Using killer set in config: {data.config.get('killer', section='general').upper()}",
                    style="green",
                )
            )
            return data.config.get("killer", section="general").upper()
        else:
            pyautogui.moveTo(x=142, y=91, duration=0.1)
            pyautogui.click()

            sleep(0.5)

            screenshot = self.sct.grab(
                {"top": 35, "left": 455, "width": 300, "height": 35}
            )

            image = Image.frombytes(
                "RGB", screenshot.size, screenshot.bgra, "raw", "BGRX"
            )
            text = reader.readtext(np.array(image), detail=0)

            if len(text) > 0:
                for killer in [killer.name for killer in data.Killer]:
                    if str(killer).lower() in text[0].lower():
                        log(
                            Text(
                                f"Detected selected killer: {killer}. Ignoring config value: {data.config.get('killer', section='general').upper()}",
                                style="green",
                            )
                        )
                        log(
                            Text(
                                f"To turn off automatic killer detection, check out the web panel settings",
                                style="green",
                            )
                        )
                        return killer

            log(
                Text(
                    f"Using killer set in config: {data.config.get('killer', section='general').upper()}",
                    style="red",
                )
            )
            return data.config.get("killer", section="general").upper()

    def check_if_banner_present(self):
        try:
            return (
                pyautogui.locateOnScreen("src/assets/banner.png", confidence=0.8)
                is not None
            )
        except:
            return False

    def close_banner(self):
        try:
            pos = pyautogui.locateOnScreen("src/assets/button_ok.png", confidence=(0.8))
            if pos != None:
                pyautogui.moveTo(pos[0] + 20, pos[1] + 20, duration=0.25)
                pyautogui.mouseDown(button="left")
                sleep(0.05)
                pyautogui.mouseUp(button="left")
                sleep(0.5)
        except:
            pass

    def check_if_in_main_menu(self):
        try:
            if (
                pyautogui.locateOnScreen("src/assets/button_play.png", confidence=0.8)
                is not None
            ):
                return True
        except:
            return False

    def enter_killer_lobby(self):
        if not data.ss.check_if_in_main_menu():
            return

        try:
            pos = pyautogui.locateOnScreen("src/assets/button_play.png", confidence=0.8)
            pyautogui.click(pos[0] + 10, pos[1] + 10)
        except:
            pass

        sleep(2)

        try:
            pos = pyautogui.locateOnScreen(
                "src/assets/button_play_killer.png", confidence=0.8
            )
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
