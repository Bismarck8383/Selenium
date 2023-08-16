from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def login(name, password):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    url = "https://parascrapear.com/login"
    driver.get(url)

    campo_nombre = driver.find_element_by_xpath("//input[@name='username']")
    campo_pswd = driver.find_element_by_xpath("//input[contains(@id,'password')]")

    time.sleep(5)
    campo_nombre.send_keys(name)
    time.sleep(5)
    campo_pswd.send_keys(password)
    time.sleep(5)

    # una de las funciones que podemos usar para utilizar scrips de javascript
    # para hacer scroll
    # driver.execute_script("windows.scrollTo(0,300)")
    driver.execute_script("alert('Hola mundo')")
    time.sleep(4)
    driver.find_element_by_xpath("//input[contains(@type,'submit')]").click()
    time.sleep(2)


if __name__ == '__main__':
    usuario = input("Introduce Usuario : ")
    paswd = input("Introduce contraseña ")
    login(usuario, paswd)
    print("Todo Ok")
