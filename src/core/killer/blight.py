from random import randint
import pyautogui
from time import sleep
from core.killer import universal
import data
from util.console import log

def rush():
    log("Blight action: Rush")

    actions = data.ss.take_and_read_actions_screenshot()

    if (len(actions) == 0):
        return
            
    if any("ATTACK" in string for string in actions):
        universal.quick_attack()
        return
    
    if any("LETHAL RUSH" in string for string in actions):
        rush_logic()
        return
    
    if any("RUSH" in string for string in actions):
        rush_logic()
        return

def rush_logic():
    # for some reason pyautogui.click, rightClick etc only trigger
    # the first rush. not sure why. so i have to "hold" the button
    pyautogui.mouseDown(button="secondary")
    sleep(0.01)
    pyautogui.mouseUp(button="secondary")