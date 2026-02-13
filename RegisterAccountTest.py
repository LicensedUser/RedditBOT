import webbrowser
import pyautogui
import time
import pyperclip
import re
import random
PassWord = ("K1S9Rbl1iw")

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

# Get text from clipboard
text = pyperclip.paste()

# Extract only numbers
numbers = re.findall(r'\d+', text)  # finds all sequences of digits

# Join all numbers together (optional)
numbers_only = ''.join(numbers)

print("Original clipboard text:", text)
print("Numbers extracted:", numbers_only)

# Press Alt + 2
pyautogui.hotkey('alt', '2')
time.sleep(2)

# Press Ctrl + F
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)

# Type "Verification code"
pyautogui.write("Verification code")
time.sleep(2)

# Press ESC
pyautogui.press('esc')
time.sleep(2)

# Press TAB
pyautogui.press('tab')
time.sleep(2)

# Type "VER CODE"
pyautogui.write(numbers_only)
time.sleep(2)

# Press ENTER
pyautogui.press('enter')
time.sleep(5)

# Press Ctrl + F
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)

# Type "Available"
pyautogui.write("available")
time.sleep(2)

# Press ESC
pyautogui.press('esc')
time.sleep(2)

# Press TAB
pyautogui.press('tab')
time.sleep(2)

# Type PassWord
pyautogui.write(PassWord)
time.sleep(2)

# Press ENTER
pyautogui.press('enter')
time.sleep(20)

times = random.randint(1, 4)

for _ in range(times):
    pyautogui.press('tab')
    time.sleep(1)
  
# Press ENTER
pyautogui.press('enter')
time.sleep(20)

# Press TAB
pyautogui.press('tab')
time.sleep(2)

# Press TAB
pyautogui.press('tab')
time.sleep(2)

# Press TAB
pyautogui.press('space')
time.sleep(2)

# Press Ctrl + F
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)

# Type "Continue"
pyautogui.write("Continue")
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
time.sleep(20)

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
time.sleep(20)

# Press ENTER
pyautogui.press('enter')
time.sleep(20)

# Press Ctrl + L
pyautogui.hotkey('ctrl', 'l')
time.sleep(2)

# Press Ctrl + C
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)

# Press ESC
pyautogui.press('esc')
time.sleep(2)

AccURL = pyperclip.paste()
with open("NewAccounts.txt", "a", encoding="utf-8") as file:
    file.write(AccURL + "\n")
  
time.sleep(2)

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
time.sleep(20)

# Press Ctrl + F
pyautogui.hotkey('ctrl', 'f')
time.sleep(2)

# Type "Log Out"
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
time.sleep(20)
