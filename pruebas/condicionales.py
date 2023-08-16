from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert


def condicionales():
    try:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        url = "https://testpages.herokuapp.com/styled/html5-form-test.html"
        driver.get(url)
        driver.maximize_window()

        # buscar el boton
        btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[contains(@class,"
                                                                                          "'styled-click-button')])["
                                                                                          "2]")))

        btn = driver.find_element_by_xpath("(//input[contains(@class,'styled-click-button')])[2]")
        buscar_btn = driver.execute_script("arguments[0].scrollIntoView();", btn)
        if btn.is_displayed() and btn.is_enabled():
            print("Boton listo para dar click")
            time.sleep(5)
            btn.click()
        else:
            print("No puede dar click en el boton")

    except TimeoutException as ex:
        print(ex.msg)

    time.sleep(3)
    print("saliendo del programa....")
    time.sleep(3)
    driver.close()


if __name__ == '__main__':
    condicionales()
