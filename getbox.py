import pyautogui

def capture_area():
  while True:
    if pyautogui.confirm("Clique em OK para capturar") == 'OK':
      x1, y1 = pyautogui.position()
      break
  
  while True:
    if pyautogui.confirm("Clique em OK para capturar") == 'OK':
      x2, y2 = pyautogui.position()
      break
  
  width = x2 - x1
  height = y2 - y1

  return (x1, y1, width, height)

if __name__ == '__main__':
  area = capture_area()
  print(area)
      