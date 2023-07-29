import json
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import psycopg2
import json

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

urls = [
    {'url': 'https://fr.hotels.com/Hotel-Search?adults=1&d1=2023-07-22&d2=2023-07-23&destination=Dakar%2C%20Dakar%20Region%2C%20S%C3%A9n%C3%A9gal&endDate=2023-07-23&flexibility=0_DAY&latLong=14.716674%2C-17.467679&regionId=1024&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2023-07-22&theme=&useRewards=false&userIntent=', 'ville': 'Dakar'},
    {'url': 'https://fr.hotels.com/Hotel-Search?adults=2&d1=2023-07-18&d2=2023-07-19&destination=Paris%2C%20France&endDate=2023-07-19&latLong=48.853564%2C2.348095&regionId=2734&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2023-07-18&theme=&useRewards=false&userIntent=', 'ville': 'Paris'},
    {'url': 'https://fr.hotels.com/Hotel-Search?adults=1&children=&d1=2023-07-22&d2=2023-07-23&destination=Londres%2C%20Angleterre%2C%20Royaume-Uni&endDate=2023-08-23&flexibility=0_DAY&latLong=51.50746%2C-0.127673&mapBounds=&pwaDialog=&regionId=2114&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2023-08-21&theme=&useRewards=false&userIntent=', 'ville': 'Londres'}
]

data = []

for url_info in urls:
    url = url_info['url']
    ville = url_info['ville']

    driver = webdriver.Firefox(options=chrome_options)
    driver.get(url)
    time.sleep(5)  # Attendre 5 secondes pour permettre le chargement des éléments

    elements = driver.find_elements(By.CSS_SELECTOR, ".uitk-layout-flex.uitk-layout-flex-block-size-full-size.uitk-layout-flex-flex-direction-column.uitk-layout-flex-justify-content-space-between")

    for element in elements:
        dicti = {}
        dicti['Ville'] = ville

        name_element = element.find_elements(By.CSS_SELECTOR, ".uitk-heading.uitk-heading-5.overflow-wrap.uitk-layout-grid-item.uitk-layout-grid-item-has-row-start")
        dicti['NomHotel'] = name_element[0].text if name_element else "N/A"

        price_element = element.find_elements(By.CSS_SELECTOR, ".uitk-text.uitk-type-600.uitk-type-bold.uitk-text-emphasis-theme")
        dicti['Prix'] = price_element[0].text if price_element else "N/A"

        rating_element = element.find_elements(By.CSS_SELECTOR, ".uitk-rating-5")
        dicti['Note'] = rating_element[0].text if rating_element else "N/A"

        location_element = element.find_elements(By.CSS_SELECTOR, ".uitk-text.uitk-text-spacing-half.truncate-lines-2.uitk-type-300.uitk-text-default-theme")
        dicti['localisa'] = location_element[0].text if location_element else "N/A"

        data.append(dicti)

    driver.quit()
    
with open('data.json', 'w') as f:
    json.dump(data, f,ensure_ascii=False)

print("Données enregistrées avec succès.")   
# conn = psycopg2.connect(
#     host="localhost",
#     database="cmd_service",
#     user="mouhamed",
#     password="Mouhamed9/"
# )
# for item in data:
#     ville = item['Ville']
#     nom_hotel = item['NomHotel']
#     prix = item['Prix']
#     note = item['Note']
#     localisation = item['localisa']

#     # Exécuter la requête SQL d'insertion
#     cursor = conn.cursor()
#     query = "INSERT INTO chambre (ville, nom_hotel, prix, note, localisation) VALUES (%s, %s, %s, %s, %s)"
#     values = (ville, nom_hotel, prix, note, localisation)
#     cursor.execute(query, values)
#     conn.commit()

# # Fermer la connexion à la base de données
# conn.close()

