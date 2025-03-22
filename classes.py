import pyautogui

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

  def volta(self):
    self.count -= 1
    self.check_tamanho()
    pyautogui.click(self.poke_posxy[self.count])

class pixel:
    def getlootbypixel(self, caixa, cor_esperada):
        try:
          x, y, largura, altura = caixa
          imagem = pyautogui.screenshot(region=(x, y, largura, altura))
          for px in range(largura):
            for py in range(altura):
              cor_pixel = imagem.getpixel((px, py))
              if cor_pixel == cor_esperada:
                centro_x = x + px
                centro_y = y + py
                pyautogui.moveTo(centro_x, centro_y)
                pyautogui.click(centro_x, centro_y)
                return True
              
        except Exception:
          return False