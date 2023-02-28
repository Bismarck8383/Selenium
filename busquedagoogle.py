from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def busqueda(palabra):
    url = "https://www.google.es/ "

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    print("Resultado : {}".format(driver))

    nombre_elemento = driver.find_element(By.NAME, "q")
    nombre_elemento.send_keys(palabra)
    time.sleep(20)
    nombre_elemento.send_keys(Keys.ENTER)


if __name__ == '__main__':
    frase = input("Que desea buscar : ")
    busqueda(frase)
