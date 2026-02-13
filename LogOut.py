import webbrowser
import pyautogui
import time

webbrowser.open("https://www.reddit.com")

# Wait 20 seconds for page to load
time.sleep(60)

# Press Ctrl + F
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)

# Type "Create"
pyautogui.write("Create")
time.sleep(2)

# Press ESC
pyautogui.press('esc')
time.sleep(2)

# Press TAB
pyautogui.press('tab')
time.sleep(2)

# Press TAB
pyautogui.press('tab')
time.sleep(2)

# Press ENTER
pyautogui.press('enter')
time.sleep(30)

# Press Ctrl + F
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)

# Type "Log Out"
pyautogui.write("Log Out")
time.sleep(2)

# Press ESC
pyautogui.press('esc')
time.sleep(2)

# Press TAB
pyautogui.press('tab')
time.sleep(2)

# Press ALT + TAB
pyautogui.hotkey('shift', 'tab')
time.sleep(2)

# Press ENTER
pyautogui.press('enter')
time.sleep(30)
