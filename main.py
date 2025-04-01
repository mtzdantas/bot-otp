from classes import setup
from classes import troca
from keyboard import is_pressed
import pyautogui
from time import sleep
from ast import literal_eval
def check_state():
  try:
    check = pyautogui.locateOnScreen('battle.png', confidence=0.9)
    if check:
      # cavebot()
      pass

  except pyautogui.ImageNotFoundException:
    battle()
  
def battle():
  pyautogui.press(['Q', 'E'])
  sleep(0.5)
  troca.ida()

def cavebot():
  global indice
  if indice < len(posicoes):
    x, y = posicoes[indice]
    pyautogui.click(x, y)
    sleep(1)
    indice += 1

  else:QE
    indice = 0
    print("Fim do percurso.")

setup = setup()

battle_box = setup.set_battle()
pyautogui.screenshot('battle.png', region=battle_box)
pokes_pos = setup.set_pokesequence()
troca = troca(pokes_pos=pokes_pos)
# arquivo = input('Qual nome do arquivo? ')
# with open(f'{arquivo}.txt', 'r') as f:
  # conteudo = f.read().strip()
  # posicoes = literal_eval(conteudo)
# indice = 0

while True:
  if is_pressed('P'):
    break
  check_state()