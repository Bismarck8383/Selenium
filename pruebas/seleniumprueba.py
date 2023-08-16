# para instalar  automáticamente chromedriver
from webdriver_manager.chrome import ChromeDriverManager
# driver de selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests

# empezamos el escraping
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
print(driver)
# url = "https://www.pccomponentes.com/tempest-f36-silla-gaming-negra-azul"
url = "https://web.whatsapp.com/"
driver.get(url)
print(driver.title)

pet = requests.get(url)
print(pet.headers)
# mostramos el código html
# driver.page_source

"""
soup = BeautifulSoup(driver.page_source, "html.parser")
precio = soup.find_all("span", class_="baseprice")
for pre in precio:
    print("Precios bases : {}".format(pre.text))
"""

print("---------Veremos las cookies--------------")
#print(pet.cookies['__cf_bm'])
# cerramos chrome
driver.quit()
