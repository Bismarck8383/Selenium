import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from multiprocessing import Process


def test_login():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    url = "https://appolow.app/#/auth/login"
    url2 = "https://appolow.app/#/"
    driver.get(url)
    assert url in driver.current_url, f"No se encontro la {url}"
    driver.find_element_by_class_name("btn-fancy").click()
    time.sleep(2)
    assert url2 in driver.current_url, f"No se entro a la URL: {url2}"
    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = Process(target=test_login)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Pruebas completadas")
