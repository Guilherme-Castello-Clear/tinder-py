import time
import pyautogui


def try_match():
    button = pyautogui.locateOnScreen('tinderbtn.png', minSearchTime=5)
    button = pyautogui.center(button)
    button_x, button_y = button
    pyautogui.click(button_x, button_y)


while True:
    try_match()
    time.sleep(1)
