import time
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from funciones.selenium_funciones import FuncionesGlobales


def test_login():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    f = FuncionesGlobales(driver=driver)
    f.navigate_to("https://testingqarvn.com.es/datos-personales/")

    f.get_path_sendkey("//input[contains(@placeholder,'Nombre:')]", "Alberto", 1)
    f.get_path_sendkey("//input[@id='wsf-1-field-22']", "Moral", 1)
    f.get_path_sendkey("(//input[@class='wsf-field'])[2]", "more@corre.com", 1)
    f.get_path_sendkey("//input[contains(@id,'wsf-1-field-24')]", "12345689", 1)
    f.get_path_sendkey("//input[contains(@id,'wsf-1-field-24')]", "12345689", 1)
    f.get_path_sendkey("//textarea[@id='wsf-1-field-28']", "campo a rellenar de datos", 1)
    f.get_path_click("//button[contains(.,'Submit')]", 1)

    driver.close()


test_login()
