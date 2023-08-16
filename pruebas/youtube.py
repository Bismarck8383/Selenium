from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def youtube(data):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    url1 = "https://www.youtube.es/"
    driver.get(url1)
    driver.maximize_window()

    driver.implicitly_wait(10)
    driver.execute_script("document.querySelector('#content.ytd-consent-bump-v2-lightbox').scrollTo(0, 200)")
    btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "yt-spec-button-shape-next--call-to-action.yt-spec-button-shape-next--filled")))
    btn.click()
    time.sleep(4)
    buscar = driver.find_element_by_xpath("//input[contains(@id,'search')]")
    buscar.send_keys(data)
    time.sleep(5)

    driver.find_element_by_xpath("(//yt-icon[contains(@class,'style-scope ytd-searchbox')])[2]").click()
    time.sleep(5)
    driver.execute_script("window.scrollTo( 0, 400 )")
    time.sleep(5)
    driver.execute_script("window.scrollTo( 0, 500 )")
    time.sleep(5)
    driver.execute_script("window.scrollTo( 0, 500 )")
    time.sleep(5)
    driver.close()


if __name__ == '__main__':
    busca = input("Que deseas ver : ")
    youtube(busca)
