from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from multiprocessing import Process


def test_login():
    edge = DesiredCapabilities.EDGE
    edge['ms:edgeOptions'] = {'w3c': True}
    edge['platformName'] = 'windows'
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=edge)

    url = "https://appolow.app/#/auth/login"
    url_home = "https://appolow.app/#/"
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    assert url in driver.current_url, f"No se encontro la {url}"
    elem_user = driver.find_element_by_xpath("//input[contains(@placeholder,'Usuario')]")
    elem_user.send_keys("appolow")
    elem_pass = driver.find_element_by_xpath("//input[contains(@type,'password')]")
    elem_pass.send_keys("44o548gakw")
    elem_pass.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.implicitly_wait(5)
    assert url_home in driver.current_url, f"No se encontro la URL : {url_home}"

    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    browsers = []
    for i in range(4):
        p = Process(target=test_login)
        browsers.append(p)
        p.start()

    for p in browsers:
        p.join()

    print("Pruebas Completadas")
