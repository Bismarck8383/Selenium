import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


class BaseTest:
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.login()

    def login(self):
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        assert url != '', "La URL está vacía"
        assert url.startswith(('http', 'https')), "La URL no es válida"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[contains(@placeholder,'Username')]").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[contains(@placeholder,'Username')]").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()
        time.sleep(2)

        print("¡Ingresaste exitosamente!")
        print(5)

        self.tearDown()

    def tearDown(self):
        time.sleep(
            10)  # Espera de 20 segundos antes de cerrar la prueba (puedes ajustar este tiempo según tus necesidades)
        self.driver.close()
        print("Cerrando Prueba ...")


if __name__ == '__main__':
    base = BaseTest()
    base.setUp()
