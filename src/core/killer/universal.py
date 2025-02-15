from random import randint
import pydirectinput
import pyautogui
from time import sleep
from util.console import log


def walk_backwards():
    pyautogui.keyDown("s")
    sleep(1)
    pyautogui.keyUp("s")


def quick_attack():
    pyautogui.mouseDown(button="left")
    sleep(0.1)
    pyautogui.mouseUp(button="left")


def basic_attack():
    pyautogui.keyDown("w")
    sleep(0.1)
    pyautogui.mouseDown(button="left")
    sleep(0.6)
    pyautogui.mouseUp(button="left")
    pyautogui.keyUp("w")


def click_disconnect_banners():
    # Coords of the "banner" (survivor disconneted etc.)
    pyautogui.click(x=1379, y=658)
    pyautogui.click(x=1379, y=658)
    # Coords of the disconnected banner (network error)
    pyautogui.click(x=1376, y=652)
    pyautogui.click(x=1376, y=652)


def walk_and_attack():
    log("Universal action: Walk and attack")
    walk_backwards()
    basic_attack()
    click_disconnect_banners()
    walk_backwards()

    sleep(4)


def attack_random_direction():
    log("Universal action: Look in random direction")

    # Short backward movement (for a lil' surprise, might hit a surv lol)
    pyautogui.keyDown("s")
    sleep(0.3)
    pyautogui.keyUp("s")

    # Look in random direction
    pydirectinput.moveRel(randint(-500, 500), 0)
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width / 2, screen_height / 2)

    basic_attack()
    walk_backwards()

    sleep(4)
