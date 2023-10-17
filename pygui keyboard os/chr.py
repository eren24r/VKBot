import keyboard 
import os 
import time
import pyautogui

os.startfile(r'"C:/Program Files/Google/Chrome/Application/chrome.exe"')
time.sleep(2)
keyboard.write("https://www.youtube.com/results?search_query=java+%D1%83%D1%80%D0%BE%D0%BA%D0%B8+alisher")
keyboard.press("enter")
time.sleep(3)
pyautogui.moveTo(800, 600, 2)
time.sleep(2)
pyautogui.click()
