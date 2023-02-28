from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert


def alertas():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    url = "https://testpages.herokuapp.com/styled/alerts/alert-test.html"
    driver.get(url)
    driver.maximize_window()

    try:

        # botonera alert
        time.sleep(5)
        btn_alert = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'alertexamples')]")))
        btn_alert = driver.find_element_by_xpath("//input[contains(@id,'alertexamples')]")
        alert = driver.execute_script("arguments[0].scrollIntoView();", btn_alert)
        btn_alert.click()
        time.sleep(5)
        # driver.switch_to_alert().accept()

        alerta = Alert(driver)
        alerta.accept()
        time.sleep(5)

        # botonera confirm
        bt_confirm = driver.find_element_by_xpath("(//input[contains(@class,'styled-click-button')])[2]")
        bt_confirm.click()
        time.sleep(5)

        confirmacion = Alert(driver)
        time.sleep(5)
        confirmacion.dismiss()  # cancelar
        time.sleep(3)

        # boton prompt
        btn_prompt = driver.find_element_by_xpath("(//input[contains(@class,'styled-click-button')])[3]")
        btn_prompt.click()
        time.sleep(3)

        input_prommpt = Alert(driver)
        input_prommpt.send_keys("Hola todos")
        time.sleep(3)
        input_prommpt.accept()
        time.sleep(3)

    except TimeoutException as ex:
        print(ex.msg)

    print("saliendo del programa....")
    time.sleep(3)


if __name__ == '__main__':
    alertas()
