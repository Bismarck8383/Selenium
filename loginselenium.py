from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def login(username, password):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    url = "https://parascrapear.com/login"
    driver.get(url)
    print("Resultado :  {}".format(driver))

    username_field = driver.find_element_by_name("username")
    password_field = driver.find_element_by_name("password")

    username_field.send_keys(username)
    password_field.send_keys(password)

    time.sleep(20)

    driver.find_element_by_xpath("//input[@value='Iniciar sesión']").click()


if __name__ == '__main__':
    usuario = input("Introduce el usuario : ")
    passw = input("Introduce Password  : " )
    login(usuario, passw)
