# TODO:
# - More killers: Dracula, 

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
import random
import datetime

Killer = Enum('Killer', ['OTHER', "TRAPPER"])

# CONFIGURATION

killer = Killer.OTHER # From the list above
stop_after_games = 100 # Script plays about 4-5 games per hour (10 minutes in game, 5 minutes in lobby)
stop_after_xp = 20000 # Script gets around 2000xp per hour

# END OF CONFIGURATION

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

State = Enum('State', ['INGAME', 'INLOBBY', 'INQUEUE'])

games = 0
xp = 0
total_time_in_game = 0

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

def perform_ingame_action():
    def walk_and_attack():
        pyautogui.keyDown("w")
        time.sleep(0.5)
        pyautogui.keyUp("w")

        pyautogui.keyDown("s")
        time.sleep(0.5)
        pyautogui.keyUp("s")

        # Coords of the "banner" (survivor disconneted etc.); if no banner is present, it just attacks like normal
        pyautogui.click(x=1379, y=658)
        pyautogui.click(x=1379, y=658)
        pyautogui.click(x=1379, y=658)
    
    def attack():
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()

    console.log(Text("Performing random movement as ") + Text(f"{killer.name}", style="bold red"))

    if (killer == Killer.OTHER):
        walk_and_attack()
    elif (killer == Killer.TRAPPER):
        random_action = random.randint(0, 1)
        if random_action == 0:
            walk_and_attack()
        else:
            pyautogui.mouseDown(button="secondary")
            time.sleep(4)
            pyautogui.mouseUp(button="secondary")
            time.sleep(2)
            pyautogui.press("space")
    time.sleep(10)

def print_stats():
    console.print("\n\n")
    console.log(Text(f" Game Time: ~{time_in_game / 60} minutes ", style="black on aqua"))
    console.log(Text(f" XP Earned: {xp} ({xp / games} average) ", style="black on yellow"))
    console.log(Text(f" Games Played: {games} ", style="black on green"))
    console.log(Text(f" Running Time: {str(datetime.timedelta(seconds=int(time.time() - script_start_time)))} ({str(datetime.timedelta(seconds=int(total_time_in_game)))} in games; {str(datetime.timedelta(seconds=int((time.time() - script_start_time) - total_time_in_game)))} in lobby)"))
    console.print("\n\n")

console = Console()

console.set_window_title("DBD Auto AFK by Pazdikan")
console.clear()
console.log(Text("Initializing..."))
console.log(Text("! IGNORE ALL ERRORS BELOW !", style="bold black on red"))

if __name__ == '__main__':
    script_start_time = time.time()
    current_state = State.INLOBBY
    
    game_started_at = None

    reader = easyocr.Reader(['en'])

    with mss.mss() as sct:
        console.clear()
        console.log(Text("Initialized!", style="green"))
        while True:
            if (games >= stop_after_games or xp >= stop_after_xp):
                console.log(Text("Stopping script due XP or Games limit set in the configuration", style="green"))
                print_stats()
                break

            if (current_state == State.INGAME):
                ocr = take_and_read_screenshot(endgame_button)

                if any("CONTINUE" in string for string in ocr):
                    time_in_game = time.time() - game_started_at

                    pyautogui.click(x=465, y=871)
                    pyautogui.click(x=465, y=871)
                    pyautogui.click(x=465, y=871)

                    time.sleep(15)

                    current_xp = take_and_read_xp_screenshot() 
                    if (len(current_xp) > 0):
                        xp += int(current_xp[0])
                    else:
                        xp += time_in_game * 0.8 # 1 second in game = 1 xp; but the time isnt perfect so reduce the xp

                    time.sleep(5)

                    click_image()
                    click_image()
                    click_image()
                    console.log("Clicking CONTINUE (endgame)")
                    current_state = State.INLOBBY

                    games += 1
                    total_time_in_game += time_in_game

                    print_stats()

                    console.log("Setting state to INLOBBY")
                    console.log("Waiting 30 seconds")
                    time.sleep(30)
                    console.log("Finished waiting")
                else:
                    perform_ingame_action()
            else:
                # When you level up your rift, the right expandable menu will cover the play button
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