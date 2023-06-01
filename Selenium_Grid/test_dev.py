from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from multiprocessing import Process


# ejecuta la prueba en navegadores de Chrome

def test_login():
    chrome = DesiredCapabilities.CHROME
    chrome['goog:chromeOptions'] = {'w3c': True}
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=chrome)

    url = "https://appolow.app/#/auth/login"
    url_home = "https://appolow.app/#/"
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    assert url in driver.current_url, f"No se encontro la {url}"
    driver.find_element_by_xpath("//input[contains(@placeholder,'Usuario')]").send_keys("appolow")
    driver.find_element_by_xpath("//input[contains(@type,'password')]").send_keys("44o548gakw")
    driver.find_element_by_class_name("btn-fancy").click()
    time.sleep(2)
    driver.implicitly_wait(5)
    assert url_home in driver.current_url, f"No se encontro la URL : {url_home}"

    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    browsers = []
    for i in range(5):
        p = Process(target=test_login)
        browsers.append(p)
        p.start()

    for p in browsers:
        p.join()

    print("Pruebas Completadas")
