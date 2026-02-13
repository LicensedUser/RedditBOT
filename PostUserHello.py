import os
import webbrowser
import pyautogui
import time
import pyperclip

# Open browser
webbrowser.open("https://chatgpt.com")

# Wait 60 seconds for page to load
time.sleep(60)

pyautogui.write('Write 1 hello post from new reddit user in csv format, ask users to engage upvote comment ,50-70 words > title,post')
time.sleep(2)

pyautogui.press('enter')
time.sleep(60)

# Press Ctrl + F
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)

# Type "Attach"
pyautogui.write("Attach")
time.sleep(2)

# Press ESC
pyautogui.press('esc')
time.sleep(2)

# Press ALT + TAB
pyautogui.hotkey('shift', 'tab')
time.sleep(2)

# Press ALT + TAB
pyautogui.hotkey('shift', 'tab')
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

# Press ENTER
pyautogui.press('enter')
time.sleep(30)

# Press Ctrl + F
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)

# Type "Title"
pyautogui.write("Title")
time.sleep(2)

# Press ESC
pyautogui.press('esc')
time.sleep(2)

# Press TAB
pyautogui.press('tab')
time.sleep(30)


