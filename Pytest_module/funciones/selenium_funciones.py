import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class FuncionesGlobales:
    def __init__(self, driver):
        self.driver = driver

    # función que inicia la navegación le pasamos la url
    def navigate_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def selector_xpath(self, path):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, path)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_xpath(path)
            return val
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontro el xpath : {path}")

    def selector_id(self, id):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element_by_id(id)
        return val

    def selector_css(self, css):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_css_selector(css)
            if val is None:
                raise AssertionError(f"No se encontró el selector : {css}")
            return val
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontró el Css selector  : {css}")

    # toma un elemento desde el xpath para darle clic
    def get_path_click(self, path, t):
        try:
            val = self.selector_xpath(path)
            if val is None:
                raise AssertionError(f"No se encontró el Path : {path}")
            val.click()
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontró el Path : {path}")

    # toma un elemento para rellenar un campo
    def get_path_sendkey(self, path, texto, t):
        try:
            val = self.selector_xpath(path)
            if val is None:
                raise AssertionError(f"No se encontró el Path del input  : {path}")
            val.send_keys(texto)
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontró el Path del input  : {path}")

    # toma un elemento desde él, Id para darle clic
    def get_id_click(self, id, t):
        try:
            val = self.selector_id(id)
            if val is None:
                raise AssertionError(f"No se encontró el ID   : {id}")
            val.click()
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el Id  : {}".format(id))

    # toma el elemento desde él, id para enviar un texto
    def get_id_sendkey(self, id, texto, t):
        try:
            val = self.selector_id(id)
            if val is None:
                raise AssertionError(f"No se encontró el ID del input  : {id}")
            val.send_keys()
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el Id  : {}".format(id))

    # toma el elemento desde el name="Nombre" para darle clic
    def get_by_name_click(self, name, t):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, name)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_name(name)
            val.click()
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el Name  : {}".format(name))

    # toma el elemento desde el name = "nombre" para enviar un texto
    def get_by_name_sendkey(self, name, texto, t):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, name)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_name(name)
            val.send_keys(texto)
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el Name  : {}".format(name))

    # toma el elemento desde la clase para darle clic
    def get_class_click(self, clase, t):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, clase)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_class_name(clase)
            val.click()
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró la clase  : {}".format(clase))

    # toma el elemento desde la clase para enviar un texto
    def get_class_sendkey(self, clase, texto, t):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, clase)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_class_name(clase)
            val.send_keys(texto)
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró la clase  : {}".format(clase))

    # tomamos el elemento desde su selector CSS para darle clic
    def get_css_selector_click(self, css, t):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_css_selector(css)
            val.click()
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el Css selector  : {}".format(css))

    # Usamos  el selector CSS para rellenar un input o text area
    def get_css_selector_senkey(self, css, texto, t):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_css_selector(css)
            val.send_keys(texto)
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el Css selector  : {}".format(css))

    # tomamos el elemento desde el nombre de etiqueta para darle clic
    def get_by_tag_name_click(self, tag, t):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, tag)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_tag_name(tag)
            val.click()
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el Tag_Name  : {}".format(tag))

    # tomamos el elemento desde su nombre de etiqueta rellena el input
    def get_by_tag_name_senkey(self, tag, texto, t):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, tag)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_tag_name(tag)
            val.send_keys(texto)
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el Tag_Name  : {}".format(tag))

    # función para darle clic a un enlace buscando desde su link de texto
    def get_by_link_text_click(self, link, t):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, link)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_link_text(link)
            val.click()
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el Link_text  : {}".format(link))

    # toma la referencia desde un link de texto para enviar datos
    def get_by_link_text_sendkey(self, link, texto, t):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, link)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_link_text(link)
            val.send_keys(texto)
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el Link_text  : {}".format(link))

    # darle click en aceptar en un alert
    def accept_alert(self):
        alert = Alert(self.driver)
        alert.accept()

    # darle denegado en un alert
    def dismiss_alert(self):
        alert = Alert(self.driver)
        alert.dismiss()

    # se usa con los select con xpath
    def select_xpath_type(self, path, tipo, dato, t):
        try:
            val = self.selector_xpath(path)
            if val is None:
                raise AssertionError(f"No se encontró el Path : {path}")
            selected = Select(val)
            if tipo == "index":
                selected.select_by_index(dato)
            if tipo == "text":
                selected.select_by_visible_text(dato)
            if tipo == "value":
                selected.select_by_value(dato)
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontró el Path : {path}")

    # se usa para los select con Id
    def select_id_type(self, id, tipo, dato, t):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_id(id)
            if val is None:
                raise AssertionError(f"No se encontró el Id : {id}")
            selected = Select(val)
            if tipo == "index":
                selected.select_by_index(dato)
            if tipo == "text":
                selected.select_by_visible_text(dato)
            if tipo == "value":
                selected.select_by_value(dato)
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontró el id : {id}")
        # se usa para los select con Id

    # se usa para los select con selector css
    def select_css_type(self, css, tipo, dato, t):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_css_selector(css)
            if val is None:
                raise AssertionError(f"No se encontró el Selector : {css}")
            selected = Select(val)
            if tipo == "index":
                selected.select_by_index(dato)
            if tipo == "text":
                selected.select_by_visible_text(dato)
            if tipo == "value":
                selected.select_by_value(dato)
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontró el selector : {css}")

    # subir un archivo desde su xpath, se le pasa la ruta
    def upload_file_xpath(self, path, ruta, t):
        try:
            val = self.selector_xpath(path)
            if val is None:
                raise AssertionError(f"No se encontró el Path del archivo: {path}")
            val.send_keys(ruta)
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontró el Path del archivo : {path}")

    # subir un archivo desde él, id, se le pasa la ruta
    def upload_file_id(self, id, ruta, t):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_id(id)
            if val is None:
                raise AssertionError(f"No se encontró el Id del archivo: {id}")
            val.send_keys(ruta)
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontró el Id del archivo : {id}")

    # seleccionar un checkbox o radio por id
    def checkbox_radio_id(self, id, t):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_id(id)
            if val is None:
                raise AssertionError(f"No se encontró el Id del checkbox o radio: {id}")
            val.click()
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontró el Id del checkbox o radio : {id}")

    # seleccionar un checkbox o radio desde un xpath
    def checkbox_radio_xpath(self, path, t):
        try:
            val = self.selector_xpath(path)
            if val is None:
                raise AssertionError(f"No se encontró el xpath del checkbox o radio: {path}")
            val.click()
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontró el xpath del checkbox o radio : {path}")

    # como seleccionar todos los checkbox o radios
    # for n in range(1, 3):
    #   self.sut.checkbox_radio_multiples_xpath(2, "(//input[contains(@type,'checkbox')])[" + str(n) + "]", )
    def checkbox_radio_multiples_xpath(self, t, *args):
        try:
            for path in args:
                val = self.selector_xpath(path)
                if val is None:
                    raise AssertionError(f"No se encontró el xpath del checkbox o radio: {path}")
                val.click()
                return time.sleep(t)
        except TimeoutException as ex:
            for path in args:
                print(ex.msg)
                print(f"No se encontró el xpath del checkbox o radio : {path}")

    # muestra el texto por ID
    def get_text_id(self, id, t):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element_by_id(id)
            if val is None:
                raise AssertionError(f"No se encontró el id : {id}")
            print(f"El texto es: {val.text}")
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontró el id : {id}")

    '''
         muestra los textos con selector css, muestra todos los elementos
        mediante el for los mostramos por ID
    '''

    def get_text_css_elements(self, selector, t):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_elements_by_css_selector(selector)
            if val is None:
                raise AssertionError(f"No se encontró el selector : {selector}")
            for indice, textos in enumerate(val):
                print(f"ID : {indice}- Texto : {textos.text}")
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontró el selector : {selector}")

    def login_simple(self, login_path, path_user, path_pswd, user, pswd, t):
        try:
            val = self.selector_xpath(login_path)
            usuario = self.driver.find_element_by_xpath(path_user)
            password = self.driver.find_element_by_xpath(path_pswd)
            if val is None:
                raise AssertionError(f"No se encontró el Path : {login_path}")
            usuario.send_keys(user)
            password.send_keys(pswd)
            val.click()
            return time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontró el path : {login_path}")
