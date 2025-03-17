from classes import main
from classes import pixel
import keyboard
import mouse
import pyautogui
import time

troca = main()
pixel = pixel()

def fullhit():
  atacklist = ['1', '2', '3', '4', '5']
  pyautogui.press(atacklist)

def loot():
  pixel.getlootbypixel(caixa=(1726, 565, 192, 462), cor_esperada=(44,118,188)) # Water Gem

mouse.on_button(fullhit,buttons=('x'), types=('down'))
while True:
  loot()

  if keyboard.is_pressed('E'):
    troca.ida()

  if keyboard.is_pressed('Q'):
    troca.volta()

  if keyboard.is_pressed('P'):
    break
