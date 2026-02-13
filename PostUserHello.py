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
