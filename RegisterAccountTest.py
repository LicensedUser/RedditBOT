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
pyautogui.write("copy")
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

# Open browser
webbrowser.open("https://www.reddit.com")
