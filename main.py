from classes import troca
from classes import pixel
import keyboard
import pyautogui
import pygetwindow as gw

def set_loot_position():
  while True:
    if pyautogui.confirm("Canto Superior Esquerdo da Área de Loot - PRESSIONE OK") == 'OK':
      x1, y1 = pyautogui.position()
      break
  
  while True:
    if pyautogui.confirm("Canto Inferior Direito da Área de Loot - PRESSIONE OK") == 'OK':
      x2, y2 = pyautogui.position()
      break
  
  width = x2 - x1
  height = y2 - y1

  return (x1, y1, width, height)

def set_firstpoke_battle():
  while True:
    if pyautogui.confirm("Posição do Primeiro Pokémon no Battle - PRESSIONE OK") == 'OK':
      x1, y1 = pyautogui.position()
      break
  
  return (x1, y1)

def set_pokesequence():
  pokes_pos = []
  for i in range(6):
    if pyautogui.confirm(f"Posição do Pokemon {i} - PRESSIONE OK") == 'OK':
      x1, y1 = pyautogui.position()
      pokes_pos.append((x1, y1))
  return pokes_pos

def battle():
  try:
    check = pyautogui.locateOnScreen('battle.png', confidence=0.9)
    if check:
      pass

  except pyautogui.ImageNotFoundException:
    pyautogui.click(firstpoke)

def fullhit():
  atacklist = ['1', '2', '3', '4', '5']
  pyautogui.press(atacklist)

def loot():
  pixel.getlootbypixel(caixa=caixa, cor_esperada=(44,118,188)) # Water Gem

nick = input('Digite o nick do seu personagem: ').capitalize()
print(nick)
caixa = set_loot_position()
firstpoke = set_firstpoke_battle()
pokes_pos = set_pokesequence()

troca = troca(pokes_pos=pokes_pos)
pixel = pixel()

while True:
  for window in gw.getWindowsWithTitle(f"otPokemon | {nick}"):
    window.activate()
  loot()
  battle()

  if keyboard.is_pressed('E'):
    troca.ida()

  if keyboard.is_pressed('Q'):
    fullhit()

  if keyboard.is_pressed('P'):
    break
