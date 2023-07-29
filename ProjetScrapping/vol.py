# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.by import By

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

# driver = webdriver.Firefox(options=chrome_options)
# driver.get('https://booking.kayak.com/flights/DSS-PAR/2023-08-10?sort=price_a')

# elements = driver.find_elements(By.CLASS_NAME, 'flights')

# elementss = []

# for element in elements:
#     valeur = element.text
#     elementss.append(valeur)

# for element in elementss:
#     print(element)

# driver.quit()


# moreButton
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

# driver = webdriver.Firefox(options=chrome_options)
# driver.get('https://booking.kayak.com/flights/DSS-PAR/2023-08-10?sort=price_a')

# while True:
#     # selecs = driver.find_elements(By.CSS_SELECTOR, '.col-field.carrier')
#     # for selec in selecs:
#     #     elements = selec.find_element(By.CLASS_NAME, 'bottom')
#     #     print(elements.text)

#     selecs = driver.find_elements(By.CLASS_NAME, 'resultInner')
#     for selec in selecs:
#         # compagnie = selec.find_element(By.CSS_SELECTOR, '.col-field.carrier').find_element(By.CLASS_NAME, 'bottom')
#         # heuredep = selec.find_element(By.CSS_SELECTOR, '.col-field.time.depart').find_element(By.CLASS_NAME, 'top')
#         # aeroportdep = selec.find_element(By.CSS_SELECTOR, '.col-field.time.depart').find_element(By.CLASS_NAME, 'bottom')
#         # heurearr = selec.find_element(By.CSS_SELECTOR, '.col-field.time.return').find_element(By.CLASS_NAME, 'top')
#         # aeroportarr = selec.find_element(By.CSS_SELECTOR, '.col-field.time.return').find_element(By.CLASS_NAME, 'bottom')
#         prix = selec.find_element(By.CLASS_NAME, 'above-button').find_element(By.CLASS_NAME, 'price-text')
#         # element2 = selec.find_element(By.CLASS_NAME, 'bottom')
#         # print(element1.text)
#         print(prix.text)

#     try:
#         more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'moreButton')))
#         more_button.click()
#         WebDriverWait(driver, 10).until(EC.staleness_of(selecs[-1]))
#     except:
#         break

# driver.quit()

import csv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Firefox(options=chrome_options)
driver.get('https://booking.kayak.com/flights/DSS-PAR/2023-08-10?sort=price_a')

donnees = []

def scraping(x):
    compagnie = x.find_element(By.CSS_SELECTOR, '.col-field.carrier').find_element(By.CLASS_NAME, 'bottom').text
    heuredep = x.find_element(By.CSS_SELECTOR, '.col-field.time.depart').find_element(By.CLASS_NAME, 'top').text
    aeroportdep = x.find_element(By.CSS_SELECTOR, '.col-field.time.depart').find_element(By.CLASS_NAME, 'bottom').text
    heurearr = x.find_element(By.CSS_SELECTOR, '.col-field.time.return').find_element(By.CLASS_NAME, 'top').text
    aeroportarr = x.find_element(By.CSS_SELECTOR, '.col-field.time.return').find_element(By.CLASS_NAME, 'bottom').text
    prix = x.find_element(By.CLASS_NAME, 'above-button').find_element(By.CLASS_NAME, 'price-text').text
    
    donnees.append([compagnie,heuredep,aeroportdep,heurearr,aeroportarr,prix])


hasNextPage = True
pageNumber = 1

while hasNextPage & pageNumber <= 10 : 
    print('Page', pageNumber)

    driver.implicitly_wait(5)
    selecs = driver.find_elements(By.CLASS_NAME, 'resultInner')

    for selec in selecs:
        scraping(selec)
    
    nextPageButton = driver.find_element(By.CLASS_NAME, 'moreButton')
    hasNextPage = nextPageButton.is_enabled()

    if hasNextPage:
        driver.execute_script("arguments[0].click();", nextPageButton)
        # Attendre que la nouvelle page se charge
        driver.implicitly_wait(5)

        pageNumber += 1 

driver.quit()
