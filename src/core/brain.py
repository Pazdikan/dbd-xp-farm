import config
from util.console import console, print_stats
from rich.text import Text
from time import time, sleep
import pyautogui
import core.behavior as behavior

def check_if_limit_reached():
    if (config.xp_limit > 0 and config.xp >= config.xp_limit):
        console.log(Text("XP limit reached. The script will now turn off", style="green"))
        return True
    
    elif (config.games_limit > 0 and config.games >= config.games_limit):
        console.log(Text("Games Played limit reached. The script will now turn off", style="green"))
        return True
    
    return False

def loop():
    if (check_if_limit_reached()):
        quit()

    if (config.current_state == config.State.INGAME):
        ocr = config.ss.take_and_read_screenshot(config.ss.endgame_button)

        if any("CONTINUE" in string for string in ocr):
            time_in_game = time() - config.game_started_at

            pyautogui.click(x=467, y=899)
            pyautogui.click(x=467, y=899)
            pyautogui.click(x=467, y=899)

            sleep(15)
            current_xp = config.ss.take_and_read_xp_screenshot() 

            if (len(current_xp) > 0):
                config.xp += int(current_xp[0])
            else:
                config.xp += time_in_game * 0.8 # "Predicted" XP gain when the OCR fails

            sleep(5)

            config.ss.click_image()
            config.ss.click_image()
            config.ss.click_image()

            console.log("Clicking CONTINUE (endgame)")
            config.current_state = config.State.INLOBBY
            config.games += 1
            config.total_time_in_game += time_in_game
            
            console.log(f"{Text('Game Finished! Earned XP: {current_xp}', style='green')}")
            print_stats()

            console.log("Setting state to INLOBBY")
            console.log("Waiting 30 seconds")
            sleep(30)
            console.log("Finished waiting")
        else:
            behavior.perform_ingame_action()
            
    else:
        # When you level up your rift, the right expandable menu will cover the play button
        # This moves the mouse to top left corner to close it
        pyautogui.moveTo(0, 0)
    
        ocr = config.ss.take_and_read_screenshot(config.ss.lobby_button)
        if any("PLAY" in string for string in ocr):
            config.ss.click_image()
            config.ss.click_image()
            config.ss.click_image()

            console.log("Clicking PLAY in main menu")
        elif any("READY" in string for string in ocr):
            config.ss.click_image()
            config.ss.click_image()
            config.ss.click_image()

            console.log("Clicking READY in found lobby")
            config.current_state = config.State.INGAME
            console.log("Setting state to INGAME")
            console.log("Waiting 120 seconds")

            sleep(120) # Loading from lobby to game (+ missing players etc.)
            console.log("Finished waiting")

            config.game_started_at = time()
        elif not ocr:                   
            ocr = config.ss.take_and_read_screenshot(config.ss.endgame_button)
            # Sometimes the game doesn't register the click
            # Script thinks it's in main menu but game is still in endgame 
            if any("CONTINUE" in string for string in ocr):
                config.ss.click_image()
                config.ss.click_image()
                config.ss.click_image()

                console.log("Clicking CONTINUE (endgame)")
                console.log("Waiting 30 seconds")
                sleep(30)
                console.log("Finished waiting")
        console.log("Waiting 5 seconds")
        sleep(5)
