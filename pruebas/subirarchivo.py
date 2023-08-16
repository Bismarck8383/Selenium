from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException


def uploadFile():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    url = "https://testpages.herokuapp.com/file_upload_j.html"
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    try:
        buscar_image = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'fileinput')]")))
        buscar_image = driver.find_element_by_xpath("//input[contains(@id,'fileinput')]")
        buscar_image.send_keys("C://Users//bismarck.colombo//Documents//Python//img//scooter.png")
        time.sleep(5)
        select_input = driver.find_element_by_xpath("//input[contains(@value,'image')]")
        select_input.click()
        time.sleep(3)
        enviar = driver.find_element_by_xpath("//input[contains(@value,'image')]")
        enviar.click()
        time.sleep(10)

    except TimeoutException as ex:
        print(ex.msg)


if __name__ == '__main__':
    uploadFile()
