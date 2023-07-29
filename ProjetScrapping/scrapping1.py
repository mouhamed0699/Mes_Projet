from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

url = 'https://fr.readytotrip.com/hotels/S%C3%A9n%C3%A9gal/Dakar/?date_from=06-07-2023&date_to=07-07-2023&adults=2&children=0'
ville = 'Dakar'

driver = webdriver.Firefox(options=chrome_options)
driver.get(url)
time.sleep(5)

elements = driver.find_elements(By.CSS_SELECTOR, ".box")

data = []

for element in elements:
    dicti = {'Ville': ville}
   

    nom_hotel = element[0].find_element(By.CSS_SELECTOR, '.box-title')
    
    dicti['NomHotel'] = nom_hotel

    print(nom_hotel.text,type(nom_hotel.text))

driver.quit()


