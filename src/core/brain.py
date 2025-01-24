import data
import overlay
from util.console import log, print_stats
from rich.text import Text
from time import time, sleep
import pyautogui
import core.behavior as behavior

def check_if_limit_reached():
    if (float(data.config.get('xp_limit', section='limits')) > 0 and data.xp >= float(data.config.get('xp_limit', section='limits'))):
        log(Text("XP limit reached. The script will now turn off", style="green"))
        return True
    
    elif (float(data.config.get('games_limit', section='limits')) > 0 and data.games >= float(data.config.get('games_limit', section='limits'))):
        log(Text("Games Played limit reached. The script will now turn off", style="green"))
        return True
    
    return False

waiting_times = 0
def loop():
    if (overlay.overlay != None):
        if (data.config.get('overlay', section='general') == "0"):
            overlay.overlay.set_visibility(False)
        elif (data.config.get('overlay', section='general') == "1"):
            overlay.overlay.set_visibility(True)


    global waiting_times
    if (check_if_limit_reached()):
        quit()

    if (data.ss.check_if_banner_present()):
        log(Text("Banner detected, trying to close it...", style="red"))
        data.ss.close_banner()
        sleep(5)
        return
    
    if (data.ss.check_if_in_main_menu()):
        log(Text("Main menu detected, trying to join killer lobby...", style="red"))
        data.ss.enter_killer_lobby()

    if (data.current_state == data.State.INGAME):
        ocr = data.ss.take_and_read_screenshot(data.ss.endgame_button)

        if any("CONTINUE" in string for string in ocr):
            if (data.game_started_at != None):
                time_in_game = time() - data.game_started_at
            else:
                time_in_game = 0

            pyautogui.click(x=472, y=899)
            pyautogui.click(x=472, y=899)
            pyautogui.click(x=472, y=899)

            log("Waiting 15 seconds for XP animation to end")

            sleep(15)
            log("Trying to get XP")
            current_xp = data.ss.take_and_read_xp_screenshot()

            if (len(current_xp) > 0):
                current_xp_int = 0
                try:
                    current_xp_int = int(current_xp[0])
                except:
                    pass

                data.xp += current_xp_int
            else:
                predicted_xp = int(time_in_game * 0.9)
                log(Text("Failed to read XP from screenshot.", style="red"))
                log(Text(f"Predicted XP gain: {predicted_xp}"))
                data.xp += predicted_xp

            sleep(1)

            log("Trying to get Bloodpoints")
            pyautogui.moveTo(411, 900, duration=0.1)
            pyautogui.click(x=411, y=900)
            pyautogui.click(x=411, y=900)
            pyautogui.click(x=411, y=900)

            sleep(5)

            current_bp = data.ss.take_and_read_bloodpoint_screenshot()
            print(current_bp)
            if (len(current_bp) > 0):
                current_bp_int = 0
                try:
                    current_bp_int = int(current_bp[0].replace(' ', ''))
                except:
                    pass

                data.bloodpoints += current_bp_int

        
            log(f"{Text(f'Game {data.games + 1}: Earned XP: {data.xp}, BP: {data.bloodpoints}', style='green')}")

            data.ss.click_image("src/assets/button_continue.png")

            log("Clicking CONTINUE (endgame)")
            data.current_state = data.State.INLOBBY
            data.games += 1
            data.total_time_in_game += time_in_game
            
            print_stats()

            log("Setting state to INLOBBY")
            log("Waiting 15 seconds")
            sleep(15)
            log("Finished waiting")
        else:
            behavior.perform_ingame_action()
            
    else:
        # When you level up your rift, the right expandable menu will cover the play button
        # This moves the mouse to top left corner to close it
        pyautogui.moveTo(0, 0, duration=0.1)
    
        ocr = data.ss.take_and_read_screenshot(data.ss.lobby_button)
        if any("PLAY" in string for string in ocr):
            data.ss.click_image("src/assets/button_queue.png")

            log("Clicking PLAY in main menu")

            data.selected_killer = data.ss.take_and_read_killer_name_screenshot()

        elif any("READY" in string for string in ocr):
            data.ss.click_image("src/assets/button_ready.png")

            log("Clicking READY in found lobby")
            data.current_state = data.State.INGAME
            log("Setting state to INGAME")
            log("Waiting 120 seconds")

            sleep(120) # Loading from lobby to game (+ missing players etc.)
            log("Finished waiting")

            data.game_started_at = time()
        elif not ocr:                   
            ocr = data.ss.take_and_read_screenshot(data.ss.endgame_button)
            # Sometimes the game doesn't register the click
            # Script thinks it's in main menu but game is still in endgame 
            if any("CONTINUE" in string for string in ocr):
                data.ss.click_image("src/assets/button_continue.png")

                log("Clicking CONTINUE (endgame)")
                log("Waiting 30 seconds")
                sleep(30)
                log("Finished waiting")
        log("Waiting 5 seconds")
        waiting_times += 1
        sleep(5)

        if (waiting_times >= 60):
            log(Text("Waited for over 10 minutes... making sure script is not in main menu (experimental feature, might fail)", style="blue"))
            waiting_times = 0
            pyautogui.moveTo(100, 100, duration=0.25)
            sleep(1)