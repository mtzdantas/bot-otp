import pyautogui

class setup:
  def set_loot_position(self):
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
  
  def set_pokesequence(self):
    pokes_pos = []
    for i in range(1, 7):
      if pyautogui.confirm(f"Posição do Pokemon {i} - PRESSIONE OK") == 'OK':
        x1, y1 = pyautogui.position()
        pokes_pos.append((x1, y1))
    
    return pokes_pos
  
  def set_battle(self):
    while True:
      if pyautogui.confirm("Canto Superior Esquerdo da Área do Battle - PRESSIONE OK") == 'OK':
        x1, y1 = pyautogui.position()
        break
    
    while True:
      if pyautogui.confirm("Canto Inferior Direito da Área do Battle - PRESSIONE OK") == 'OK':
        x2, y2 = pyautogui.position()
        break
    
    width = x2 - x1
    height = y2 - y1

    return (x1, y1, width, height)
  
class troca:
  def __init__(self, pokes_pos):
    self.count = 0
    self.poke_posxy = pokes_pos

  def check_tamanho(self):
    self.count = self.count % len(self.poke_posxy)
  
  def ida(self):
    self.count += 1
    self.check_tamanho()
    pyautogui.click(self.poke_posxy[self.count])