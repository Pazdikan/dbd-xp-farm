import os
import sys
import mss
import cv2
import ctypes
import psutil
import numpy as np
import pyautogui
import pytesseract
from PIL import Image

from time import sleep
from colorama import Fore, init
from pynput.keyboard import Controller, Listener
init(convert=True)
system = os.name

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return False;
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return True;

def main():
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)

    print(f"{Fore.MAGENTA}Auto AFK is running!{Fore.RESET}")

    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 1000, "left": 1640, "width": 200, "height": 50}


        while True:
            # Grab the data
            sct_img = sct.grab(monitor)

            # Save to the picture file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output="screenshot.png")

            text = pytesseract.image_to_string(Image.open("screenshot.png"))

            if text != None and "READY" in text:
                if (text != "UNREADY"):
                    pyautogui.click(x=1775, y=1026)
                    pyautogui.moveTo(0, 0)
                    print("Clicking ready in lobby.")

            if text != None and "CONTINUE" in text:
                pyautogui.click(x=1775, y=1026)
                pyautogui.moveTo(0, 0)
                print("Clicking continue post game.")

            sleep(10)

if __name__ == "__main__":
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW("DBD Auto AFK | Made By Pazdikan")
    elif system == 'posix':
        os.system("\033]0;DBD Auto AFK | Made By Pazdikan\a")

    main()
