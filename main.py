from classes import setup
from classes import troca
import keyboard
import pyautogui
import time

def battle():
  try:
    check = pyautogui.locateOnScreen('battle.png', confidence=0.9)
    if check:
      pass

  except pyautogui.ImageNotFoundException:
    time.sleep(1)
    pyautogui.press(['Q', 'E'])
    troca.ida()

setup = setup()

battle_box = setup.set_battle()
pyautogui.screenshot('battle.png', region=battle_box)
pokes_pos = setup.set_pokesequence()
troca = troca(pokes_pos=pokes_pos)

while True:
  if keyboard.is_pressed('P'):
    break

  battle()