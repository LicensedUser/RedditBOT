import webbrowser
import pyautogui
import time

# Open browser
webbrowser.open("https://temp-mail.org/en")

# Wait 20 seconds for page to load
time.sleep(20)

# Press Ctrl + F
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)

# Type "copy"
pyautogui.write("Copy")
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
time.sleep(2)

# Open browser
webbrowser.open("https://www.reddit.com")

# Wait 20 seconds for page to load
time.sleep(20)

# Press Ctrl + F
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)

# Type "copy"
pyautogui.write("Log In")
time.sleep(2)

# Press ESC
pyautogui.press('esc')
time.sleep(2)

# Press ENTER
pyautogui.press('enter')
time.sleep(2)

# Press Ctrl + F
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)

# Type "Sign Up"
pyautogui.write("Sign Up")
time.sleep(2)

# Press ESC
pyautogui.press('esc')
time.sleep(2)

# Press ALT + TAB
pyautogui.hotkey('shift', 'tab')
time.sleep(2)

# Press ENTER
pyautogui.press('enter')
time.sleep(10)

# Press Ctrl + F
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)

# Type "Already a"
pyautogui.write("Already a")
time.sleep(2)

# Press ESC
pyautogui.press('esc')
time.sleep(2)

# Press ALT + TAB
pyautogui.hotkey('shift', 'tab')
time.sleep(2)

# Press CTRL + v
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# Press ENTER
pyautogui.press('enter')
time.sleep(10)

# Press Alt + 1
pyautogui.hotkey('alt', '1')
time.sleep(2)

# Press Ctrl + F
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)

# Type "Reddit"
pyautogui.write("Reddit")
time.sleep(2)

# Press ESC
pyautogui.press('esc')
time.sleep(2)

pyautogui.keyDown('shift')
time.sleep(1)
pyautogui.press('down')
time.sleep(1)
pyautogui.press('down')
time.sleep(1)
pyautogui.press('down')
time.sleep(1)
pyautogui.keyUp('shift') 
time.sleep(2)

# Press CTRL + c
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)
