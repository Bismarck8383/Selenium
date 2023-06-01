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
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to(self, url):
        assert url != '', "La URL está vacía"
        assert url.startswith(('http', 'https')), "La URL no es válida"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_visibility_of_element(self, locator, locator_type=By.XPATH):
        return self.wait.until(EC.visibility_of_element_located((locator_type, locator)))

    def find_element(self, locator, locator_type):
        assert locator != '', "Locator cannot be empty"
        element = self.wait_for_visibility_of_element(locator, locator_type)
        self.scroll_into_view(element)
        return element

    def selector_xpath(self, path):
        return self.find_element(path, By.XPATH)

    def selector_id(self, id):
        return self.find_element(id, By.ID)

    def selector_css(self, css):
        return self.find_element(css, By.CSS_SELECTOR)

    def selector_name(self, name):
        return self.find_element(name, By.NAME)

    def selector_class_name(self, clase):
        return self.find_element(clase, By.CLASS_NAME)

    def selector_tag_name(self, tag):
        return self.find_element(tag, By.TAG_NAME)

    def selector_link_text(self, link):
        return self.find_element(link, By.LINK_TEXT)

    # toma un elemento desde el xpath para darle clic
    def get_path_click(self, path, t):
        assert t >= 0, "El tiempo de espera no puede ser negativo"
        try:
            val = self.selector_xpath(path)
            val.click()
            time.sleep(t)
        except AssertionError as ae:
            print(ae)
            print(f"No se encontró el Path : {path}")
        except TimeoutException as ex:
            print(f"No se encontró el Path : {path}, TimeoutException: {ex}")

    # toma un elemento para rellenar un campo
    def get_path_sendkey(self, path, texto, t):
        assert t >= 0, "El tiempo de espera no puede ser negativo"
        try:
            val = self.selector_xpath(path)
            val.send_keys(texto)
            time.sleep(t)
        except AssertionError as ae:
            print(ae)
            print(f"No se encontró el Path del input  : {path}")
        except TimeoutException as ex:
            print(f"No se encontró el Path del input  : {path}, TimeoutException: {ex}")

    # toma un elemento desde él, Id para darle clic
    # hacer clic en el elemento por su ID
    def get_id_click(self, id, t):
        assert t >= 0, "El tiempo de espera no puede ser negativo"
        try:
            val = self.selector_id(id)
            val.click()
            time.sleep(t)
        except AssertionError as ae:
            print(ae)
            print(f"No se encontró el ID: {id}")
        except TimeoutException as ex:
            print(f"No se encontró el ID: {id}, TimeoutException: {ex}")

    # enviar un texto al elemento por su ID
    def get_id_sendkey(self, id, texto, t):
        assert t >= 0, "El tiempo de espera no puede ser negativo"
        try:
            val = self.selector_id(id)
            val.send_keys(texto)
            time.sleep(t)
        except AssertionError as ae:
            print(ae)
            print(f"No se encontró el ID del input: {id}")
        except TimeoutException as ex:
            print(f"No se encontró el ID del input: {id}, TimeoutException: {ex}")

    # toma el elemento desde el name="Nombre" para darle clic
    # hacer clic en el elemento por su nombre
    def get_by_name_click(self, name, t):
        assert t >= 0, "El tiempo de espera no puede ser negativo"
        try:
            val = self.selector_name(name)
            val.click()
            time.sleep(t)
        except AssertionError as ae:
            print(ae)
            print(f"No se encontró el Name: {name}")
        except TimeoutException as ex:
            print(f"No se encontró el Name: {name}, TimeoutException: {ex}")

    # enviar un texto al elemento por su nombre
    def get_by_name_sendkey(self, name, texto, t):
        assert t >= 0, "El tiempo de espera no puede ser negativo"
        try:
            val = self.selector_name(name)
            val.send_keys(texto)
            time.sleep(t)
        except AssertionError as ae:
            print(ae)
            print(f"No se encontró el Name del input: {name}")
        except TimeoutException as ex:
            print(f"No se encontró el Name del input: {name}, TimeoutException: {ex}")

    # toma el elemento desde la clase para darle clic
    # hacer clic en el elemento por su clase
    def get_class_click(self, clase, t):
        assert t >= 0, "El tiempo de espera no puede ser negativo"
        try:
            val = self.selector_class(clase)
            val.click()
            time.sleep(t)
        except AssertionError as ae:
            print(ae)
            print(f"No se encontró la clase: {clase}")
        except TimeoutException as ex:
            print(f"No se encontró la clase: {clase}, TimeoutException: {ex}")

    # enviar un texto al elemento por su clase
    def get_class_sendkey(self, clase, texto, t):
        assert t >= 0, "El tiempo de espera no puede ser negativo"
        try:
            val = self.selector_class(clase)
            val.send_keys(texto)
            time.sleep(t)
        except AssertionError as ae:
            print(ae)
            print(f"No se encontró la clase del input: {clase}")
        except TimeoutException as ex:
            print(f"No se encontró la clase del input: {clase}, TimeoutException: {ex}")

    # hacer clic en el elemento por su selector CSS
    def get_css_selector_click(self, css, t):
        assert t >= 0, "El tiempo de espera no puede ser negativo"
        try:
            val = self.selector_css(css)
            val.click()
            time.sleep(t)
        except AssertionError as ae:
            print(ae)
            print(f"No se encontró el selector CSS: {css}")
        except TimeoutException as ex:
            print(f"No se encontró el selector CSS: {css}, TimeoutException: {ex}")

    # enviar un texto al elemento por su selector CSS
    def get_css_selector_sendkey(self, css, texto, t):
        assert t >= 0, "El tiempo de espera no puede ser negativo"
        try:
            val = self.selector_css(css)
            val.send_keys(texto)
            time.sleep(t)
        except AssertionError as ae:
            print(ae)
            print(f"No se encontró el selector CSS del input: {css}")
        except TimeoutException as ex:
            print(f"No se encontró el selector CSS del input: {css}, TimeoutException: {ex}")

    # tomamos el elemento desde el nombre de etiqueta para darle clic
    # Hacer click en el elemento por su nombre de etiqueta
    def get_by_tag_name_click(self, tag, t):
        assert t >= 0, "El tiempo de espera no puede ser negativo"
        try:
            val = self.selector_tag_name(tag)
            val.click()
            time.sleep(t)
        except AssertionError as ae:
            print(ae)
            print(f"No se encontró el nombre de la etiqueta: {tag}")
        except TimeoutException as ex:
            print(f"No se encontró el nombre de la etiqueta: {tag}, TimeoutException: {ex}")

    # Enviar un texto al elemento por su nombre de etiqueta
    def get_by_tag_name_sendkey(self, tag, texto, t):
        assert t >= 0, "El tiempo de espera no puede ser negativo"
        try:
            val = self.selector_tag_name(tag)
            val.send_keys(texto)
            time.sleep(t)
        except AssertionError as ae:
            print(ae)
            print(f"No se encontró el nombre de la etiqueta del input: {tag}")
        except TimeoutException as ex:
            print(f"No se encontró el nombre de la etiqueta del input: {tag}, TimeoutException: {ex}")

    # función para darle clic a un enlace buscando desde su link de texto
    # Hacer clic en el elemento por su texto de enlace
    def get_by_link_text_click(self, link, t):
        assert t >= 0, "El tiempo de espera no puede ser negativo"
        try:
            val = self.selector_link_text(link)
            val.click()
            time.sleep(t)
        except AssertionError as ae:
            print(ae)
            print(f"No se encontró el texto del enlace: {link}")
        except TimeoutException as ex:
            print(f"No se encontró el texto del enlace: {link}, TimeoutException: {ex}")

    # Enviar un texto al elemento por su texto de enlace
    def get_by_link_text_sendkey(self, link, texto, t):
        assert t >= 0, "El tiempo de espera no puede ser negativo"
        try:
            val = self.selector_link_text(link)
            val.send_keys(texto)
            time.sleep(t)
        except AssertionError as ae:
            print(ae)
            print(f"No se encontró el texto del enlace del input: {link}")
        except TimeoutException as ex:
            print(f"No se encontró el texto del enlace del input: {link}, TimeoutException: {ex}")

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
        assert t >= 0, "El tiempo de espera no puede ser negativo"
        try:
            val = self.selector_xpath(path)
            selected = Select(val)
            if tipo == "index":
                selected.select_by_index(int(dato))  # asegurando que el dato sea un entero
            elif tipo == "text":
                selected.select_by_visible_text(str(dato))  # asegurando que el dato sea una cadena
            elif tipo == "value":
                selected.select_by_value(str(dato))  # asegurando que el dato sea una cadena
            else:
                raise ValueError("El tipo especificado no es válido: debe ser 'index', 'text' o 'value'")
            time.sleep(t)
        except AssertionError as ae:
            print(ae)
            print(f"No se encontró el Path : {path}")
        except ValueError as ve:
            print(ve)
        except TimeoutException as ex:
            print(f"No se encontró el Path : {path}, TimeoutException: {ex}")

    # se usa para los select con Id
    def select_id_type(self, id, tipo, dato, t):
        assert t >= 0, "El tiempo de espera no puede ser negativo"
        assert tipo in ["index", "text", "value"], "El tipo de selección no es válido"

        val = self.selector_id(id)
        if val is None:
            raise AssertionError(f"No se encontró el Id : {id}")

        selected = Select(val)
        if tipo == "index":
            selected.select_by_index(dato)
        elif tipo == "text":
            selected.select_by_visible_text(dato)
        elif tipo == "value":
            selected.select_by_value(dato)

        time.sleep(t)

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
