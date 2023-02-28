import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from funciones.selenium_funciones import FuncionesGlobales

f = ""
driver = ""


def setup_funcion():
    global f
    global driver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    f = FuncionesGlobales(driver=driver)
    f.navigate_to("https://www.saucedemo.com/")


def teardown_funcion():
    print("Fin del test")
    time.sleep(3)
    driver.close()


def test_uno():
    f.get_path_sendkey("//input[contains(@id,'user-name')]", "Alberto", 1)
    f.get_path_sendkey("//input[@data-test='password']", "admin123", 1)
    f.get_path_click("//input[contains(@data-test,'login-button')]", 1)


if __name__ == '__main__':
    setup_funcion()
    test_uno()
    teardown_funcion()
