import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from funciones.selenium_funciones import FuncionesGlobales


class base_test(unittest.TestCase):

    def setUp(self):
        print("----------------------------")
        print("Iniciando prueba")
        print("----------------------------")
        user_agente = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/109.0.0.0 Safari/537.36"}
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-agent={user_agente}")
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-notifications")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--no-sandbox")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--no-first-run")
        options.add_argument("--no-proxy-server")
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        self.driver = driver
        self.sut = FuncionesGlobales(driver=driver)

    def test_1(self):
        self.sut.navigate_to("https://www.geeksforgeeks.org/how-to-use-xpath-with-beautifulsoup/")

    def tearDown(self):
        time.sleep(20)
        driver = self.driver
        driver.close()
        print("Cerrando Prueba ...")


if __name__ == '__main__':
    unittest.main()
