from selenium import webdriver
import pyautogui
import time
from selenium.webdriver.common.keys import Keys
from colored import fg, bg, attr
from selenium.webdriver.common.by import By
##############################################################
color = fg('red')
color2 = fg('blue')
#############################################################
logo = '''
 _          __  _____   _       _____   _____       ___  ___   _____  
| |        / / | ____| | |     /  ___| /  _  \     /   |/   | | ____| 
| |  __   / /  | |__   | |     | |     | | | |    / /|   /| | | |__   
| | /  | / /   |  __|  | |     | |     | | | |   / / |__/ | | |  __|  
| |/   |/ /    | |___  | |___  | |___  | |_| |  / /       | | | |___  
|___/|___/     |_____| |_____| \_____| \_____/ /_/        |_| |_____|                                                                                                                                                  
'''
print(color + logo)
pseudo = input("que voulez vous rechercher ?:")
print(color2, 'MESSAGE BIEN RECU !, veuillez patienter...')
time.sleep(5)
pyautogui.press('win')
time.sleep(5)
pyautogui.write('chrome', interval=0.25)
time.sleep(6)
pyautogui.press('enter')
time.sleep(6)
pyautogui.write("www.youtube.com", interval=0.25)
time.sleep(2)
pyautogui.press('enter')
time.sleep(10)
pyautogui.click(1214, 34)
time.sleep(8)
pyautogui.click(388, 132)
time.sleep(2)
pyautogui.write(pseudo, interval=0.25)
time.sleep(4)
pyautogui.press('enter')



