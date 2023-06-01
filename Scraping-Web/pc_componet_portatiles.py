import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from funciones.selenium_funciones import FuncionesGlobales
from prettytable import PrettyTable


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
        options.add_argument("--headless")
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
        busqueda = input("Ingrese el producto a buscar : ")
        self.sut.navigate_to("https://www.pccomponentes.com/portatiles")
        #product-card
        product_titles = self.driver.find_elements_by_class_name("product-card__title")
        # product_prices = self.driver.find_elements_by_class_name("sc-gJLAYP")
        found = False
        table = PrettyTable(['Producto'])
        for title in product_titles:
            if busqueda.lower() in title.text.lower():
                table.add_row([title.text])
                found = True
        if found:
            print(table)
        else:
            print(f"No se encontraron productos que contengan '{busqueda}'")

    def tearDown(self):
        time.sleep(5)
        driver = self.driver
        driver.close()
        print("Cerrando Prueba ...")


if __name__ == '__main__':
    unittest.main()
