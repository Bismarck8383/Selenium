import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from multiprocessing import Process


def test_login():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    url = "https://testluis-appolow.apps.lowcode-dev.bosonit.local/#/auth/login"
    url_home = "https://testluis-appolow.apps.lowcode-dev.bosonit.local/#/"
    driver.get(url)
    assert url in driver.current_url, f"No se encontro  la {url}"
    user = driver.find_element_by_xpath("//input[contains(@placeholder,'Usuario')]")
    psw = driver.find_element_by_xpath("//input[contains(@type,'password')]")
    user.send_keys("admin")
    psw.send_keys("admin")
    driver.find_element_by_xpath("//button[@class='btn btn-fancy w-100']").click()
    time.sleep(2)
    assert url_home in driver.current_url, f"No encontro la url de home {url_home}"
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

