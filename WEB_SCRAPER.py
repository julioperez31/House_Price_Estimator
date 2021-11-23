import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_argument("--enable-javascript")
driver = webdriver.Chrome(options=options)
tipo_propiedad = []
sector = []
precio = []
cant_habi = []
banos = []
espacio = []
url = 'https://www.remaxrd.com/propiedades/q:%22%22+business:sale+perPage:24/?'
driver.get(url)
delay = 30
error =['<span class="bathrooms"><i class="icon icon-remax-bathroom"></i> 2 2</span>','<span class="bathrooms"><i class="icon icon-remax-bathroom"></i> 2</span>']
ScrollNumber = 100
for i in range(1,ScrollNumber):
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.card__content')))
        driver.execute_script("window.scrollTo(1,50000)")
        time.sleep(10)
        content = driver.page_source
        soup = BeautifulSoup(content,features="lxml")
        for a in soup.findAll('div', attrs={'class': 'card__content'}):
            tipo = a.find('p', attrs={'class': 'mg0 card__description__title'})
            lugar = a.find('p', attrs={'class': 'card__description__address__mansory'})
            price = a.find('p', attrs={'class': 'card__description__price'})
            habi = a.find('span', attrs={'class': 'rooms'})
            bano = a.find('span', attrs={'class': 'bathrooms'})
            tamano = a.find('span', attrs={'class': 'sqm-construction'})
            if banos is not None and habi is not None:

                tipo_propiedad.append(tipo.text)
                sector.append(lugar.text)
                precio.append(price.text)
                cant_habi.append(habi.text)
                banos.append(bano.text)
                espacio.append(tamano.text)



    except TimeoutException:
        print("Loading took too much time!")
        pass


df = pd.DataFrame({'Tipo Propiedad': tipo_propiedad, 'Sector': sector,
                   'Precio': precio, 'Habitaciones': cant_habi,
                   'Baños': banos, 'Construccion(mt)': espacio})
df.to_excel('products.xlsx', index=False, encoding='utf-8')
