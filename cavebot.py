import pyautogui
import keyboard

try:
  posicoes = []
  arq = input('Qual nome do arquivo? ')
  option = pyautogui.confirm("Pressione OK para iniciar.\nPressione 'C' para capturar a posição do mouse ou 'ESC' para sair.")
  if option == 'OK':
    while True:
      keyboard.read_event()
      if keyboard.is_pressed('esc'):
        break
      if keyboard.is_pressed('c'):
        x, y = pyautogui.position()
        posicoes.append((x, y))
        print(f"Posição capturada: ({x}, {y})")
              
    with open(f'{arq}.txt', 'w') as f:
      f.write(str(posicoes))
         
  else:
    print("Operação cancelada.")
except KeyboardInterrupt:
  print("\nCaptura de posições interrompida.")
