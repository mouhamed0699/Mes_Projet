import json
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

urls = [
    {'url': 'https://www.kayak.com/hotels/Dakar,Senegal-c28457/2023-07-07/2023-07-08/2adults?sort=rank_a', 'ville': 'Dakar'},
    {'url': 'https://www.kayak.com/hotels/Paris,France-c36014/2023-07-07/2023-07-08/2adults?sort=rank_a', 'ville': 'Paris'},
    {'url': 'https://www.kayak.com/hotels/London,England,United-Kingdom-c28501/2023-07-07/2023-07-08/2adults?sort=rank_a=', 'ville': 'Londres'},
    {'url': 'https://www.kayak.com/hotels/Dakar,Senegal-c28457/2023-07-07/2023-07-10/2adults?sort=rank_a', 'ville': 'Dakar'},
    {'url': 'https://www.kayak.com/hotels/Paris,France-c36014/2023-07-07/2023-07-10/2adults?sort=rank_a', 'ville': 'Paris'},
    {'url': 'https://www.kayak.com/hotels/London,England,United-Kingdom-c28501/2023-07-07/2023-07-10/2adults?sort=rank_a', 'ville': 'Londres'}
]

data = []

for url_info in urls:
    url = url_info['url']
    ville = url_info['ville']
    driver = webdriver.Firefox(options=chrome_options)
    driver.get(url)
    time.sleep(10)

    # Attendre que la page se charge
    time.sleep(5)

    wait = WebDriverWait(driver, 10)

    elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".kzGk-resultInner")))

    for element in elements:
        dicti = {}
        dicti['Ville'] = ville
        dicti['prix'] = element.find_element(By.CSS_SELECTOR, ".zV27-price").text
        dicti['NomHotel'] = element.find_element(By.CSS_SELECTOR, ".FLpo-big-name").text
        dicti['Note'] = element.find_element(By.CSS_SELECTOR, ".FLpo-score-description").text

        # Vérifier si l'élément de localisation est présent avant de l'extraire
        try:
            dicti['localisation'] = element.find_element(By.CSS_SELECTOR, ".FLpo-location-name").text
        except :
            dicti['localisation'] = "N/A"

        dicti['image'] = element.find_element(By.CSS_SELECTOR, ".e9fk-photo").get_attribute("src")
        data.append(dicti)

    driver.quit()

print(data)

with open('dataNormal.json', 'w') as f:
    json.dump(data, f)
