import webbrowser
import pyautogui
import time

webbrowser.open("https://www.wikipedia.org")
time.sleep(10)

# Press ALT + F
pyautogui.hotkey('alt', 'f')
time.sleep(2)

for _ in range(4):
    pyautogui.press('right')
    time.sleep(1)

pyautogui.press('down')
time.sleep(2)
pyautogui.press('enter')

for _ in range(5):
    pyautogui.press('tab')
    time.sleep(1)

pyautogui.press('space')
time.sleep(2)

pyautogui.press('tab')
time.sleep(2)

pyautogui.press('tab')
time.sleep(2)

pyautogui.press('enter')
time.sleep(2)

# Press CTRL + W
pyautogui.hotkey('ctrl', 'w')
time.sleep(2)
