import pyautogui
import win32gui
from time import sleep

while True:
    window = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(window)

    # Check if the focused window is "DeadByDaylight-Win64-Shipping.exe" or titled "DeadByDaylight"
    if "DeadByDaylight" in window_title:
        pyautogui.mouseDown(x=682, y=563)
        sleep(0.1)
        pyautogui.mouseUp(x=682, y=563)
    
    sleep(0.5)