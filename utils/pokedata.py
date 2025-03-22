import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def dados_pokemon():
  try:
    nome_pokemon = driver.find_element(By.CLASS_NAME, 'mw-page-title-main').text

    span_moveset = driver.find_element(By.ID, 'Moveset_Padrão')

    table = span_moveset.find_element(By.XPATH, './ancestor::h2/following-sibling::table[1]')

    rows = table.find_elements(By.XPATH, './/tbody/tr')

    spells = []

    for i in range(0, len(rows), 2):
      tds = rows[i].find_elements(By.TAG_NAME, 'td')
            
      if len(tds) >= 2:
        spell_num = tds[0].text
        spell_name = tds[1].text
        spells.append({'numero': spell_num, 'nome': spell_name})
    return nome_pokemon, spells
   

  except Exception as e:
    print(f'Erro ao extrair dados: {e}')

if __name__ == '__main__':
  driver = webdriver.Chrome()
  url = 'https://wiki.otpokemon.com/index.php/Primeira_Gera%C3%A7%C3%A3o'
  driver.get(url)
  pokemons_json = []

  pokes = driver.find_elements(By.CLASS_NAME, 'square-box-pokedex')
  for card in pokes:
    card.click()
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, 'Moveset_Padrão'))
    )

    nome, spells = dados_pokemon()

    pokemons_json.append({
      'Nome': nome,
      'Ataques': spells
    })
    driver.back()
  
  driver.quit()

  with open('pokedex.json', 'w', encoding='utf-8') as f:
    json.dump(pokemons_json, f, indent=4, ensure_ascii=False)
