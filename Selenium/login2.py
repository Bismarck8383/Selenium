import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class BaseTest:
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def login(self):
        driver = self.driver

        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        url_login = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        current_page = driver.current_url
        assert url != '', "La URL está vacía"
        assert url.startswith(('http', 'https')), "La URL no es válida"
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        time.sleep(2)

        assert url == url_login, f"La URL es: {current_page} "

        driver.find_element(By.XPATH, "//input[contains(@placeholder,'Username')]").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[contains(@placeholder,'Username')]").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()
        time.sleep(2)

        dashboard_page = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

        assert dashboard_page == current_page, f"No estas dentro,  estas en : {current_page}"

        print("¡Ingresaste exitosamente!")
        print(5)

    def tearDown(self):
        time.sleep(10)  # Espera de 10 segundos antes de cerrar la prueba (puedes ajustar este tiempo según tus necesidades)
        self.driver.close()
        print("Cerrando Prueba ...")


if __name__ == '__main__':
    # Ejemplo de uso de la clase BaseTest
    base_test = BaseTest()
    try:
        base_test.setUp()
        base_test.login()

    except Exception as e:
        print(f"Se produjo un error: {e}")

    finally:
        base_test.tearDown()
