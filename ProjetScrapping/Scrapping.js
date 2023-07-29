const fs = require('fs');
const { Builder, By } = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');

const options = new firefox.Options();
options.headless();

const urls = [
  {
    url: 'https://fr.hotels.com/Hotel-Search?adults=1&d1=2023-07-22&d2=2023-07-23&destination=Dakar%2C%20Dakar%20Region%2C%20S%C3%A9n%C3%A9gal&endDate=2023-07-23&flexibility=0_DAY&latLong=14.716674%2C-17.467679&regionId=1024&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2023-07-22&theme=&useRewards=false&userIntent=',
    ville: 'Dakar'
  },
  {
    url: 'https://fr.hotels.com/Hotel-Search?adults=2&d1=2023-07-18&d2=2023-07-19&destination=Paris%2C%20France&endDate=2023-07-19&latLong=48.853564%2C2.348095&regionId=2734&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2023-07-18&theme=&useRewards=false&userIntent=',
    ville: 'Paris'
  },
  {
    url: 'https://fr.hotels.com/Hotel-Search?adults=1&children=&d1=2023-07-22&d2=2023-07-23&destination=Londres%2C%20Angleterre%2C%20Royaume-Uni&endDate=2023-08-23&flexibility=0_DAY&latLong=51.50746%2C-0.127673&mapBounds=&pwaDialog=&regionId=2114&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2023-08-21&theme=&useRewards=false&userIntent=',
    ville: 'Londres'
  }
];

async function scrapeData() {
  const data = [];

  const driver = await new Builder().forBrowser('firefox').setFirefoxOptions(options).build();

  for (const urlInfo of urls) {
    const { url, ville } = urlInfo;

    await driver.get(url);
    await driver.sleep(5000); // Attendre 5 secondes pour permettre le chargement des éléments

    const elements = await driver.findElements(By.css('.uitk-layout-flex.uitk-layout-flex-block-size-full-size.uitk-layout-flex-flex-direction-column.uitk-layout-flex-justify-content-space-between'));

    for (const element of elements) {
      const dicti = {};
      dicti['Ville'] = ville;

      const nameElement = await element.findElements(By.css('.uitk-heading.uitk-heading-5.overflow-wrap.uitk-layout-grid-item.uitk-layout-grid-item-has-row-start'));
      dicti['NomHotel'] = nameElement.length ? await nameElement[0].getText() : 'N/A';

      const priceElement = await element.findElements(By.css('.uitk-text.uitk-type-600.uitk-type-bold.uitk-text-emphasis-theme'));
      dicti['Prix'] = priceElement.length ? await priceElement[0].getText() : 'N/A';

      const ratingElement = await element.findElements(By.css('.uitk-rating-5'));
      dicti['Note'] = ratingElement.length ? await ratingElement[0].getText() : 'N/A';

      const locationElement = await element.findElements(By.css('.uitk-text.uitk-text-spacing-half.truncate-lines-2.uitk-type-300.uitk-text-default-theme'));
      dicti['localisa'] = locationElement.length ? await locationElement[0].getText() : 'N/A';

      data.push(dicti);
    }
  }

  await driver.quit();

  // Enregistrer les données dans un fichier JSON
  fs.writeFileSync('data.json', JSON.stringify(data));

  console.log('Scraping terminé. Les données ont été enregistrées dans le fichier "data.json".');
}

scrapeData();
