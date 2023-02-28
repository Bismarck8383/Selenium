from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException


def usetry(enla):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    url = "https://parascrapear.com/"
    driver.get(url)
    driver.maximize_window()

    try:
        autores = driver.find_elements_by_class_name("author")
        for tag in autores:
            print("Autores : {}".format(tag.text))
        print("La cantidad de Autores es de : {} ".format(len(autores)))

        print("---------------------------------------")
        links = driver.find_elements(By.TAG_NAME, "a")
        print("El numero de enlaces es de : {} ".format(len(links)))
        for num in links:
            href = num.get_attribute("href")
            print("Enlace  : {} ".format(num.text))
            print("Href  : {}".format(href))
            print("--------------------------------")
        driver.find_element_by_link_text(enla).click()
        time.sleep(10)
    except TimeoutException as ex:
        print(ex.msg)


if __name__ == '__main__':
    enlace = input("Cual enlace desea ver :  ")
    usetry(enlace)
    print("Saliendo del programa")
