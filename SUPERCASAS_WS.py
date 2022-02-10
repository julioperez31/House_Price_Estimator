import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
options = webdriver.ChromeOptions()
options.add_argument("--enable-javascript")
driver = webdriver.Chrome(options=options)

tipo_propiedad = []
sector = []
precio = []
datos_gen = []
url = 'https://www.supercasas.com/buscar/?PriceType=400&PagingPageSkip=1'
driver.get(url)
delay = 10

content = driver.page_source
soup = BeautifulSoup(content,features="lxml")

while True:

    try:
        for i in soup.findAll('li', attrs={'class': ['normal', 'normal video']}):
            tipo_propiedad.append(i.find('div', attrs={'class': 'type'}))
            sector.append(i.find('div', attrs={'class': 'title1'}))
            precio.append(i.find('div', attrs={'class': 'title2'}))
            datos_gen.append(i.find_all('label'))
        driver.find_element_by_xpath("//a[contains(text(),'»')]").click()
        time.sleep(3)
    except NoSuchElementException:
        print("Exiting. Last page")
        break

df = pd.DataFrame({'Tipo Propiedad': tipo_propiedad, 'Sector': sector,
                   'Precio': precio, 'Datos generales': datos_gen})
df['fecha_extraccion'] = pd.to_datetime("today")
df.to_excel('products_sc.xlsx', index=False, encoding='utf-8')
