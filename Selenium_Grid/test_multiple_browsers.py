from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from multiprocessing import Process, Queue


def test_login(browser_name, queue):
    if browser_name == "chrome":
        caps = DesiredCapabilities.CHROME
        caps['goog:chromeOptions'] = {'w3c': True}
    elif browser_name == "edge":
        caps = DesiredCapabilities.EDGE
        caps['ms:edgeOptions'] = {'w3c': True}
        caps['platformName'] = 'windows'

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=caps)

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
    queue.put(1)


if __name__ == '__main__':
    q = Queue()

    chrome_processes = []
    for i in range(2):
        p = Process(target=test_login, args=("chrome", q))
        chrome_processes.append(p)
        p.start()

    edge_processes = []
    for i in range(2):
        p = Process(target=test_login, args=("edge", q))
        edge_processes.append(p)
        p.start()

    for p in chrome_processes:
        p.join()

    for p in edge_processes:
        p.join()

    print("Pruebas Completadas")
    while not q.empty():
        q.get()
