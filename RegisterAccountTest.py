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

# Type "copy"
pyautogui.write("Sign Up")
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
time.sleep(10)

# Press Ctrl + F
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)

# Type "copy"
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
