from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


def formulario(name, password, textare):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    url = "https://testpages.herokuapp.com/styled/basic-html-form-test.html"
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)

    try:
        # rellenamos username
        usernamein = driver.find_element_by_xpath("(//input[contains(@type,'text')])[1]")
        buscar_username = driver.execute_script("arguments[0].scrollIntoView();", usernamein)
        usernamein.send_keys(name)
        print("Nombre introducido")
        time.sleep(3)

        # rellenar password
        passwordin = driver.find_element_by_xpath("(//input[contains(@size,'15')])[2]")
        buscar_passwd = driver.execute_script("arguments[0].scrollIntoView();", passwordin)
        passwordin.send_keys(password)
        print("Passwd introducida")
        time.sleep(3)

        # rellar textarea
        textarein = driver.find_element_by_xpath("//textarea[@name='comments']")
        buscar_textarea = driver.execute_script("arguments[0].scrollIntoView();", textarein)
        textarein.send_keys(textare)
        print("Rellenado textarea")
        time.sleep(3)

        # subir archivo
        subir_file = driver.find_element_by_xpath("//input[contains(@type,'file')]")
        buscar_file = driver.execute_script("arguments[0].scrollIntoView();", subir_file)
        subir_file.send_keys("C://Users//bismarck.colombo//Documents//Python//img//scooter.png")
        print("Archivo subido")
        time.sleep(3)

        # select checkbox
        checkbox = driver.find_element_by_xpath("//input[contains(@value,'cb1')]")
        buscar_checbox = driver.execute_script("arguments[0].scrollIntoView();", checkbox)
        checkbox.click()
        print("Check box seleccionado...")
        time.sleep(3)

        # select radio
        checradio = driver.find_element_by_xpath("(//input[contains(@type,'radio')])[2]")
        buscar_radio = driver.execute_script("arguments[0].scrollIntoView();", checradio)
        checradio.click()
        print("Check Radio seleccionado...")
        time.sleep(5)

        # select dropdown
        dropdown = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//select[contains(@name,'dropdown')]")))
        dropdown = driver.find_element_by_xpath("//select[contains(@name,'dropdown')]")
        ds = Select(dropdown)
        ds.select_by_visible_text("Drop Down Item 5")
        time.sleep(3)
        ds.select_by_index(2)
        print("Dropdown seleccionado")
        time.sleep(3)

        # seleccionar dentro del select
        item = Select(driver.find_element_by_name("multipleselect[]"))
        item.select_by_index(1)
        print("select seleccionado")
        time.sleep(3)

        # enviar formulario
        submit = driver.find_element_by_xpath("//input[contains(@type,'submit')]")
        submit.click()
        print("Formulario enviado")
        time.sleep(3)

    except TimeoutException as ex:
        print(ex.msg)

    print("Saliendo del programa ......")
    time.sleep(10)
    driver.close()


if __name__ == '__main__':
    username = input("Nombre  : ")
    passwd = input("Contraseña  : ")
    textarea = input("textarea  : ")

    formulario(username, passwd, textarea)
