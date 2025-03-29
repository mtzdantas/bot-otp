import pyautogui

try:
  posicoes = []
  arq = input('Qual nome do arquivo?')
  while True:
    option = pyautogui.confirm("Selecione OK para começar e clique na posição desejada!")
    if option == 'OK':
      x, y = pyautogui.position()
    posicoes.append((x, y))
    with open(f'{arq}.txt', 'a') as f:
      f.write(f"{x},{y}\n")
except KeyboardInterrupt:
  print("\nCaptura de posições interrompida.")
  print(f"Total de {len(posicoes)} posições salvas em '{arq}.txt'.")
