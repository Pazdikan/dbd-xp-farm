import mss
import pyautogui
import easyocr
import time
from PIL import Image
import os
from enum import Enum
import rich
from rich.console import Console
from rich.text import Text

pyautogui.FAILSAFE = False

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

killer_name = {
    "top": 1000,
    "left": 1650,
    "width": 235,
    "height": 35
}

State = Enum('State', ['INGAME', 'INLOBBY', 'INQUEUE'])

Killer = Enum('Killer', ['OTHER', "TRAPPER"])

games = 0
xp = 0

def click_image():
    try:
        pos = pyautogui.locateOnScreen('screenshot.png', confidence=(0.8))
        if pos != None:
            pyautogui.click(pos[0] + 20, pos[1])
            time.sleep(0.5)
    except:
        pass

def take_and_read_screenshot(area):
    screenshot = sct.grab(area)
    image = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
    image.save("screenshot.png")
    return reader.readtext("screenshot.png", detail=0)

def take_and_read_xp_screenshot():
    screenshot = sct.grab({
        "top": 700,
        "left": 540,
        "width": 75,
        "height": 35
    })
    image = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
    image.save("last_game_xp.png")
    return reader.readtext("last_game_xp.png", detail=0)

console = rich.console.Console()
console.set_window_title("DBD Auto AFK by Pazdikan")
console.clear()
console.log(Text("Initializing..."))
console.log(Text("! IGNORE ALL ERRORS BELOW !", style="bold black on red"))

if __name__ == '__main__':
    current_state = State.INGAME
    current_killer = Killer.OTHER

    game_started_at = None

    reader = easyocr.Reader(['en'])

    with mss.mss() as sct:
        console.clear()
        console.log(Text("Initialized!", style="green"))
        while True:
            if (current_state == State.INGAME):
                ocr = take_and_read_screenshot(endgame_button)

                if any("CONTINUE" in string for string in ocr):
                    time_in_game = time.time() - game_started_at

                    pyautogui.click(x=465, y=871)
                    pyautogui.click(x=465, y=871)
                    pyautogui.click(x=465, y=871)

                    time.sleep(15)

                    xp += int(take_and_read_xp_screenshot()[0])

                    time.sleep(5)

                    click_image()
                    click_image()
                    click_image()
                    console.log("Clicking CONTINUE (endgame)")
                    current_state = State.INLOBBY

                    games += 1
                    console.print("\n\n")
                    console.log(Text(f" Game Time: ~{time_in_game / 60} minutes", style="black on aqua"))
                    console.log(Text(f" XP Earned: {xp} ", style="black on yellow"))
                    console.log(Text(f" Games Played: {games} ", style="black on green"))
                    console.print("\n\n")
                    console.log("Setting state to INLOBBY")
                    console.log("Waiting 30 seconds")
                    time.sleep(30)
                    console.log("Finished waiting")
                else:
                    console.log("Performing random movement")
                    pyautogui.keyDown("w")
                    pyautogui.mouseDown()
                    time.sleep(0.5)
                    pyautogui.mouseUp()
                    pyautogui.keyUp("w")
                    time.sleep(10)
            else:
                # When you level up your rift, the right expandable menu will be shown
                # This moves the mouse to top left corner to close it
                pyautogui.moveTo(0, 0)
            
                ocr = take_and_read_screenshot(lobby_button)

                if any("PLAY" in string for string in ocr):
                    click_image()
                    click_image()
                    click_image()
                    console.log("Clicking PLAY in main menu")

                elif any("READY" in string for string in ocr):
                    click_image()
                    click_image()
                    click_image()
                    console.log("Clicking READY in found lobby")
                    current_state = State.INGAME
                    console.log("Setting state to INGAME")
                    console.log("Waiting 120 seconds")
                    time.sleep(120) # Loading from lobby to game (+ missing players etc.)
                    console.log("Finished waiting")
                    game_started_at = time.time()

                elif not ocr:                   
                    ocr = take_and_read_screenshot(endgame_button)

                    # Sometimes the game doesn't register the click
                    # Script thinks it's in main menu but game is still in endgame 
                    if any("CONTINUE" in string for string in ocr):
                        click_image()
                        click_image()
                        click_image()
                        console.log("Clicking CONTINUE (endgame)")

                        console.log("Waiting 30 seconds")
                        time.sleep(30)
                        console.log("Finished waiting")

                console.log("Waiting 5 seconds")
                time.sleep(5)