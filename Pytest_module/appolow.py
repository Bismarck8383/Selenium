import time
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from funciones.selenium_funciones import FuncionesGlobales
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
fu = FuncionesGlobales(driver=driver)


def setup_method():
    print("iniciando")


def get_data():
    return [
        ("appolow", "44o548gakw")
    ]


@pytest.mark.parametrize("usuario, clave", get_data())
def test_login(usuario, clave, ):
    fu.navigate_to("https://appolow.app/#/auth/login")

    user = driver.find_element_by_xpath("//input[contains(@formcontrolname,'username')]").clear()
    pwd = driver.find_element_by_xpath("//input[contains(@formcontrolname,'password')]").clear()
    fu.get_path_sendkey("//input[contains(@formcontrolname,'username')]", usuario, 1)
    fu.get_path_sendkey("//input[contains(@formcontrolname,'password')]", clave, 1)
    fu.get_class_click("btn_primary", 1)
    time.sleep(2)
    body = driver.find_element_by_tag_name("body")
    body.send_keys(Keys.F5)
    time.sleep(3)
    test_new_app()


# crea una nueva aplicación
def test_new_app():
    fu.get_path_click("//button[contains(@class,'mat-menu-trigger main-logo profile ng-star-inserted')]", 1)
    fu.get_path_click("//button[contains(@class,'btn ng-star-inserted')]", 2)
    # damos nombre a la app
    fu.get_path_sendkey("//input[@id='nameInput']", "bootQA", 1)
    # elejir icono
    fu.get_path_click("(//span[contains(@class,'mat-button-toggle-label-content')])[7]", 1)
    # estilo de la app
    fu.checkbox_radio_xpath("//input[contains(@id,'themeRadioEstilo minimalista')]", 1)
    # clic aceptar
    fu.get_path_click("//button[contains(@class,'btn_primary accept')]", 1)
    time.sleep(1)
    test_crear_entitty()


# crea una nueva tabla
def test_crear_entitty():
    # desplegamos el nav izquierdo
    fu.get_path_click("//mat-icon[@role='img'][contains(.,'play_arrow')]", 1)
    # damos click en nuestra app creada
    fu.get_path_click("//label[@title='bootQA']", 1)
    # damos click boton de databases
    fu.get_css_selector_click("button.mat-tooltip-trigger:first-child", 1)
    # clic botón crear nueva entidad
    fu.get_css_selector_click("button.btn-fancy:last-child", 1)
    # limpiar y rellenar campo Nombre Entidad
    limpiar_entidad = driver.find_element_by_xpath("//input[contains(@formcontrolname,'name')]")
    limpiar_entidad.clear()
    fu.get_path_sendkey("//input[contains(@formcontrolname,'name')]", "usuario", 1)
    # limpiar y rellenar campo visible
    limpiar_visible = driver.find_element_by_xpath("//input[contains(@formcontrolname,'publicName')]")
    limpiar_visible.clear()
    fu.get_path_sendkey("//input[contains(@formcontrolname,'publicName')]", "Usuario", 1)
    # le damos guardar los cambios
    fu.get_css_selector_click("button.btn_primary:first-child", 1)
    time.sleep(2)
    test_crear_campos()


# datos de campos a crear tabla usuario
def get_usuario():
    return [
        ("nombre", "Nombre"),
        ("apellidos", "Apellidos")

    ]


# funcion que crea campos
def test_new_campo(name, public):
    # boton nuevo campo
    fu.get_css_selector_click("button.btn-fancy", 1)
    # limpiar y rellenar campo nombre
    limpiar_name_campo = driver.find_element_by_xpath("//input[contains(@formcontrolname,'name')]")
    limpiar_name_campo.clear()
    fu.get_path_sendkey("//input[contains(@formcontrolname,'name')]", name, 1)
    # limpiar y rellenar campo visible
    limpiar_visible_campo = driver.find_element_by_css_selector("input.ng-invalid:last-child")
    limpiar_visible_campo.clear()
    fu.get_css_selector_senkey("input.ng-invalid:last-child", public, 1)
    # seleccionar con el select
    fu.select_css_type("select.form-select", "index", 3, 2)
    fu.select_css_type("select.form-select", "index", 0, 2)
    # clic checbox
    fu.checkbox_radio_xpath("(//span[@class='mat-checkbox-inner-container'])[1]", 1)
    # clic guardar
    fu.get_css_selector_click("button.btn_primary:nth-child(1)", 1)


# funcion que ejecuta un bucle para crear varios campos
def test_crear_campos():
    # clic boton configurar campos
    fu.get_path_click("(//button[contains(@class,'btn btn-link action')])[1]", 1)
    datos = get_usuario()

    for name, public in datos:
        test_new_campo(name, public)

    # después de crear los campos crearemos el módulo de
    time.sleep(2)
    test_crear_modulo()


def test_crear_modulo():
    # crea modulo- clic boton nuevo modulo
    fu.get_css_selector_click(".container-modules button", 1)
    # rellenar campo nombre modulo
    fu.get_path_sendkey("//input[contains(@id,'nameInput')]", "Usuario", 1)
    # selecionar icono de modulo
    fu.get_path_click("(//span[contains(@class,'mat-button-toggle-label-content')])[13]", 1)
    # clic aceptar y guardar
    fu.get_path_click("//button[contains(@class,'btn_primary accept')]", 1)
    test_crear_pagina("Add Usuario")


# creamos una página de trabajo
def test_crear_pagina(name):
    # acceder a crear pagina
    fu.get_path_click("(//button[contains(@role,'menuitem')])[2]", 1)
    # clic nueva pagina
    fu.get_path_click("//button[contains(@class,'mat-focus-indicator mat-menu-item cdk-focused cdk-mouse-focused')]", 2)
    # rellenar campo nombre pagina
    fu.get_path_sendkey("//input[contains(@formcontrolname,'name')]", name, 1)
    # elegimos área de trabjo
    fu.get_path_click("(//span[contains(@class,'mat-button-toggle-label-content')])[1]", 1)
    # damos clic en aceptar o guardar
    fu.get_css_selector_click(".btn_primary", 1)
    test_drag_drop_form()


def test_drag_drop_form():
    time.sleep(2)

    elemento_mover = fu.selector_xpath("//img[@src='assets/images/widgets/form-widget.svg']")
    # ubicar la zona donde se soltará el elemento
    zona_soltar = fu.selector_css("app-page-slot")
    # crear una instancia de ActionChains
    acciones = ActionChains(driver=driver)
    time.sleep(2)
    # realizar la acción de arrastrar y soltar
    acciones.click_and_hold(elemento_mover)
    acciones.move_to_element(zona_soltar)
    acciones.release(zona_soltar)
    acciones.perform()
    time.sleep(3)
    # damos nombre al formulario
    fu.get_path_sendkey("//input[@formcontrolname='name']", "New Usuario", 1)
    # damos clic al selector
    fu.get_css_selector_click("#mat-select-value-1", 1)
    # seleccionamos entidad
    fu.get_path_click("(//span[contains(@class,'mat-option-text')])[1]", 1)
    fu.get_path_click("//div[contains(@id,'mat-select-value-3')]", 1)
    fu.get_path_click('//*[@id="mat-option-5"]/span', 1)
    # damos clic en crear
    fu.get_path_click("//button[@class='btn_primary accept']", 1)
    time.sleep(1)
    test_second_page()


# acceder a crear pagina
def test_second_page():
    fu.get_path_click("(//button[contains(@role,'menuitem')])[2]", 1)
    # clic nueva pagina
    fu.get_path_click("//button[contains(@class,'mat-focus-indicator mat-menu-item cdk-focused cdk-mouse-focused')]", 2)
    # rellenar campo nombre pagina
    fu.get_path_sendkey("//input[contains(@formcontrolname,'name')]", "Ver Usuarios", 1)
    # elegimos área de trabjo
    fu.get_path_click("(//span[contains(@class,'mat-button-toggle-label-content')])[1]", 1)
    # damos clic en aceptar o guardar
    fu.get_css_selector_click(".btn_primary", 1)
    test_drag_drop_table()


def test_drag_drop_table():
    elemento_mover = fu.selector_xpath("//img[@src='assets/images/widgets/table-widget.svg']")
    # ubicar la zona donde se soltará el elemento
    zona_soltar = fu.selector_css("app-page-slot")
    # crear una instancia de ActionChains
    acciones = ActionChains(driver=driver)
    time.sleep(2)
    # realizar la acción de arrastrar y soltar
    acciones.click_and_hold(elemento_mover)
    acciones.move_to_element(zona_soltar)
    acciones.release(zona_soltar)
    acciones.perform()
    time.sleep(3)
    # damos nombre al formulario
    fu.get_path_sendkey("//input[@formcontrolname='name']", "Usuarios", 1)
    # damos clic al selector
    fu.get_css_selector_click("#mat-select-10", 1)
    # seleccionamos data origin
    fu.get_path_click("(//span[contains(@class,'mat-option-text')])[1]", 1)

    fu.get_css_selector_click("mat-select#mat-select-12", 1)
    fu.get_path_click("(//span[contains(.,'Usuario')])[2]", 1)
    # damos clic en crear
    fu.get_path_click("//button[@class='btn_primary accept']", 1)
    time.sleep(1)
    test_desplegar_app()


def test_desplegar_app():
    fu.get_css_selector_click("button.mat-tooltip-trigger:last-child", 2)
    time.sleep(2)
    fu.get_css_selector_click("div.deploy-app-action .content-right button", 1)

    teardown_method()


def teardown_method():
    print("Cerrando la APP")
    time.sleep(5)
    driver.close()


if __name__ == '__main__':
    setup_method()
    test_login()
