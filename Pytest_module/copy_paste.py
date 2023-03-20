import time
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from funciones.selenium_funciones import FuncionesGlobales
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
import pyperclip

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
fu = FuncionesGlobales(driver=driver)


def test_copy_paste():
    time.sleep(2)
    fu.navigate_to("https://testingqarvn.com.es/datos-personales/")
    fu.get_path_sendkey("(//input[contains(@type,'text')])[1]", "Bismarck", 1)
    inp = driver.find_element_by_xpath("//h2[contains(.,'Datos Personales Básicos')]")
    time.sleep(5)

    # Seleccionamos lo que copiaremos
    copia = inp.text
    if copia == "":
        print("el elemento esta vació")
    else:
        print(copia)
    pyperclip.copy(copia)

    # destino
    des = driver.find_element_by_xpath("//input[contains(@id,'wsf-1-field-22')]")

    # pegar
    des.send_keys(Keys.CONTROL, 'v')
    time.sleep(5)
    teardown_method()


def teardown_method():
    time.sleep(5)
    driver.close()


if __name__ == '__main__':
    test_copy_paste()
