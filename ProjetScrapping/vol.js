const { Builder, By, Key, until } = require('selenium-webdriver');
const fs = require('fs');

async function initializeDriver() {
    let driver = await new Builder().forBrowser('firefox').build();
    return driver;
}

async function runScraping() {
    let driver = await initializeDriver();

    try {
        await driver.get('https://booking.kayak.com/flights/DSS-PAR/2023-08-10?sort=price_a');

        let hasNextPage = true;
        let pageNumber = 1;
        let tab = [];

        while (hasNextPage && pageNumber <= 300) {
            console.log('Page', pageNumber);

            // Attendre que les annonces se chargent
            await driver.wait(until.elementLocated(By.className('resultInner')), 10000);

            // Récupérer tous les éléments d'annonce
            let selecs = await driver.findElements(By.className('resultInner'));

            // Parcourir les annonces et extraire les informations souhaitées
            for (let selec of selecs) {
                let compagnie = await selec.findElement(By.className('col-field carrier')).findElement(By.className('bottom')).getText();
                let heuredep = await selec.findElement(By.className('col-field time depart')).findElement(By.className('top')).getText();
                let aeroportdep = await selec.findElement(By.className('col-field time depart')).findElement(By.className('bottom')).getText();
                let heurearr = await selec.findElement(By.className('col-field time return')).findElement(By.className('top')).getText();
                let aeroportarr = await selec.findElement(By.className('col-field time return')).findElement(By.className('bottom')).getText();
                let prix = await selec.findElement(By.className('above-button')).findElement(By.className('price-text')).getText();

                // console.log(compagnie, ' ', heuredep, ' ', aeroportdep, ' ', heurearr, ' ', aeroportarr, ' ', prix);

                tab.push({ compagnie, heuredep, aeroportdep, heurearr, aeroportarr, prix });
            }

            // Vérifier s'il y a une page suivante
            let nextPageButton = await driver.findElement(By.className('moreButton'));
            hasNextPage = await nextPageButton.isEnabled();

            // Si une page suivante existe, cliquer dessus
            if (hasNextPage) {
                await driver.executeScript("arguments[0].click();", nextPageButton);

                // Attendre que la nouvelle page se charge
                await driver.wait(until.elementLocated(By.className('resultInner')), 5000);
            }

            pageNumber++;
        }

        let jsonData = JSON.stringify(tab);

        fs.writeFile('data.json', jsonData, 'utf8', (err) => {
            if (err) {
                console.error('Une erreur s\'est produite lors de l\'écriture du fichier JSON :', err);
                return;
            }
            console.log('Les données ont été enregistrées dans le fichier JSON avec succès.');
        });
    } 
    finally {
        await driver.quit();
    }
}

runScraping();
