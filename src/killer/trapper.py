import pyautogui
from time import sleep
from util.console import console

def place_and_pick_trap():
    console.log("Trapper action: Place and pick trap")

    pyautogui.mouseDown(button="secondary")
    sleep(4)
    pyautogui.mouseUp(button="secondary")
    sleep(2)
    pyautogui.press("space")