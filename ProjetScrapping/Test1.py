import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import json


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Firefox(options=chrome_options)

driver.get('https://www.liligo.fr/cars/sc.jsp?pickLocationName=Marseille%2C+Marseille+Provence+Airport&pickLocationCode=2%2C30001096%2C40001061&pickUpCountry=FR&dropLocationName=Marseille%2C+Marseille+Provence+Airport&dropLocationCode=2%2C30001096%2C40001061&dropOffCountry=FR&pickYear=2023&pickMonth=6&pickDay=21&pickHour=10&pickMinute=0&dropYear=2023&dropMonth=6&dropDay=21&dropHour=18&dropMinute=0&driverAge=26&source=carSEO#/car/results')

hasNextPage = True
pageNumber = 1
processedPages = 0

donnees = []

while hasNextPage and processedPages < 8:
    time.sleep(5)
    # print('Page :', pageNumber)
    ensemble = driver.find_elements(By.CLASS_NAME, 'car-result-item')

    for i in ensemble:
        try:
            modele_element = i.find_element(By.CLASS_NAME, 'car-result-item__model-name-text')
            Prix_element = i.find_element(By.CLASS_NAME, 'car-result-item__highlighted-price')
            image_element = i.find_element(By.TAG_NAME, 'img')

            modele = modele_element.text
            Prix = Prix_element.text
            image = image_element.get_attribute('ng-src')


            donnees.append({
                'modele': modele,
                'prix': Prix,
                'image': image
            })

            # print(modele, '', Prix, '', image)
        except StaleElementReferenceException:
            continue

    nextPageButton = driver.find_element(By.CLASS_NAME, 'simple-pagination__more-button')
    hasNextPage = nextPageButton.is_enabled()

    if hasNextPage:
        driver.execute_script("arguments[0].click();", nextPageButton)
        # Attendre que la nouvelle page se charge
        time.sleep(5)

        pageNumber += 1
        processedPages += 1

with open('djily.json', 'w') as f:
    json.dump(donnees, f, ensure_ascii=False, indent=4)
