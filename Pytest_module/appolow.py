import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from funciones.selenium_funciones import FuncionesGlobales

chrome_options = Options()
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
fu = FuncionesGlobales(driver=driver)

driver.find_element_by_xpath("(//span[contains(@class,'ud-text-sm header--dropdown-button-text--2OxOV')])[2]")

def setup_method():
    print("iniciando")


"""
def get_data():
    return [
        ("appolow", "44o548gakw")
    ]

"""


# @pytest.mark.parametrize("usuario, clave", get_data())
# def test_login(usuario, clave):
def test_login():
    fu.navigate_to("https://appolow.app/#/auth/login")

    # user = driver.find_element_by_xpath("//input[contains(@formcontrolname,'username')]").clear()
    # driver.find_elements_by_css_selector("form.ng-pristine :nth-child(1) apw-input").clear()
    # pwd = driver.find_element_by_xpath("//input[contains(@formcontrolname,'password')]").clear()
    # driver.find_elements_by_css_selector("form.ng-pristine :nth-child(2) apw-input").clear()
    # fu.get_css_selector_senkey("form.ng-pristine :nth-child(1) apw-input", "appolow", 1)
    # fu.get_css_selector_senkey("form.ng-pristine :nth-child(2) apw-input", "44o548gakw", 1)
    fu.get_class_click("btn-fancy", 1)
    time.sleep(2)
    test_new_app()


# crea una nueva aplicación
def test_new_app():
    fu.get_path_click("/html/body/app-root/appollow-wrapper/mat-sidenav-container/mat-sidenav[1]/div/div/button/button",
                      1)
    fu.get_path_click(
        "/html/body/app-root/appollow-wrapper/mat-sidenav-container/mat-sidenav[1]/div/div/div[2]/appollow-profile-menu/button",
        2)
    # clic crear nueva app
    fu.get_css_selector_click("div.company-menu-item-contaienr button:nth-child(4)", 1)
    # damos nombre a la app
    fu.get_path_sendkey("(//input[contains(@type,'text')])[1]", "bootQA", 1)
    # elejir icono
    fu.get_path_click("(//span[contains(@class,'mat-button-toggle-label-content')])[7]", 1)
    # estilo de la app
    fu.checkbox_radio_xpath("//input[contains(@id,'themeRadioEstilo minimalista')]", 1)
    # clic aceptar
    fu.get_path_click("//button[contains(@class,'btn btn-fancy')]", 1)
    test_crear_entitty()


# crea una nueva tabla
def test_crear_entitty():
    # damos click en nuestra app creada
    fu.get_path_click("//label[@title='bootQA']", 1)
    # damos click boton de databases
    fu.get_css_selector_click("button.mat-tooltip-trigger:first-child", 1)
    # clic botón crear nueva entidad
    fu.get_css_selector_click("button.btn-fancy:last-child", 1)
    # limpiar y rellenar campo Nombre Entidad
    limpiar_entidad = fu.selector_xpath("(//input[contains(@class,'form-control ng-star-inserted')])[1]")
    limpiar_entidad.clear()
    fu.get_path_sendkey("(//input[contains(@class,'form-control ng-star-inserted')])[1]", "usuario", 1)
    # limpiar y rellenar campo visible
    limpiar_visible = fu.selector_xpath("(//input[contains(@class,'form-control ng-star-inserted')])[2]")
    limpiar_visible.clear()
    ele_vi = driver.find_element_by_xpath("(//input[contains(@class,'form-control ng-star-inserted')])[2]")
    ele_vi.send_keys("user")
    # le damos guardar los cambios
    time.sleep(1)
    fu.get_css_selector_click("div.justify-content-center button.btn-fancy:nth-child(2)", 1)
    fu.get_css_selector_click("div.justify-content-center button.btn-fancy:nth-child(2)", 1)
    test_crear_campos()


# datos de campos a crear tabla usuario
def get_usuario():
    return [
        ("nombre", "nombre"),
        ("apellidos", "apellidos")

    ]


# funcion que crea campos
def test_new_campo(name, public):
    # boton nuevo campo
    fu.get_css_selector_click("button.btn-fancy", 1)
    # limpiar y rellenar campo nombre
    limpiar_name_campo = fu.selector_xpath("(//input[contains(@class,'form-control ng-star-inserted')])[1]")
    limpiar_name_campo.clear()
    fu.get_path_sendkey("(//input[contains(@class,'form-control ng-star-inserted')])[1]", name, 1)
    # limpiar y rellenar campo visible
    limpiar_visible_campo = fu.selector_xpath("(//input[contains(@class,'form-control ng-star-inserted')])[2]")
    limpiar_visible_campo.clear()
    fu.get_path_sendkey("(//input[contains(@class,'form-control ng-star-inserted')])[2]", public, 1)
    # seleccionar con el select
    # Hacer clic en el elemento
    combobox = driver.find_element_by_xpath("//div[@role='combobox']")
    combobox.click()

    # Navegar a la segunda opción
    input_element = driver.switch_to.active_element
    # input_element.send_keys(Keys.ARROW_DOWN)
    # input_element.send_keys(Keys.ARROW_DOWN)

    # Hacer clic en la segunda opción
    input_element.send_keys(Keys.RETURN)

    # clic checbox
    fu.checkbox_radio_xpath("(//input[contains(@class,'form-check-input')])[1]", 1)
    # clic guardar
    fu.get_css_selector_click("div.justify-content-end button.btn-fancy:nth-child(1)", 1)
    # fu.get_css_selector_click("div.justify-content-end button.btn-fancy:nth-child(1)", 1)


# function que ejecuta un bucle para crear varios campos
def test_crear_campos():
    # clic boton configurar campos
    fu.get_path_click("(//span[contains(@class,'button-label ng-tns-c68-12 ng-star-inserted')])[1]", 1)
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
    fu.get_path_sendkey("//input[contains(@class,'form-control ng-star-inserted')]", "Usuario", 1)
    # selecionar icono de modulo
    fu.get_path_click("(//span[contains(@class,'mat-button-toggle-label-content')])[13]", 1)
    # clic aceptar y guardar
    fu.get_path_click("//button[@class='btn btn-fancy'][contains(.,'Accept')]", 1)

    test_crear_pagina("Add Usuario")


# creamos una página de trabajo
def test_crear_pagina(name):
    # acceder a crear pagina
    fu.get_path_click("(//button[contains(@role,'menuitem')])[2]", 1)
    # clic nueva pagina
    fu.get_path_click("//button[contains(@class,'mat-focus-indicator mat-menu-item cdk-focused cdk-mouse-focused')]", 2)
    # rellenar campo nombre pagina
    fu.get_path_sendkey("//input[contains(@class,'form-control ng-star-inserted')]", name, 1)
    # elegimos área de trabjo
    fu.get_path_click("(//span[contains(@class,'mat-button-toggle-label-content')])[1]", 1)
    # damos clic en aceptar o guardar
    fu.get_css_selector_click("button.btn-fancy", 1)
    test_drag_drop_form()


def test_drag_drop_form():
    time.sleep(1)
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
    fu.get_path_sendkey("(//input[contains(@type,'text')])[1]", "New Usuario", 1)
    # damos clic al selector
    # Encontrar el elemento
    elemento = fu.selector_css('ng-select.ng-select-searchable')
    # Hacer clic en el elemento
    elemento.click()
    time.sleep(1)
    # Seleccionar la primera opción
    opcion = fu.get_css_selector_click('ng-dropdown-panel .ng-option:nth-child(1)', 1)
    # opcion.click()

    # seleccionamos entidad
    fu.get_path_click("(//span[contains(@class,'ng-arrow-wrapper')])[2]", 1)
    # Navegar a la primera opción de entidad
    input_element = driver.switch_to.active_element
    input_element.send_keys(Keys.ARROW_DOWN)

    # Hacer clic en la primera opción entidad
    input_element.send_keys(Keys.RETURN)

    # damos clic en crear
    fu.get_css_selector_click("div.d-flex button.btn-fancy.accept", 1)
    time.sleep(1)
    test_second_page()


# acceder a crear pagina
def test_second_page():
    fu.get_path_click("(//button[contains(@role,'menuitem')])[2]", 1)
    # clic nueva pagina
    fu.get_path_click("//button[contains(@class,'mat-focus-indicator mat-menu-item cdk-focused cdk-mouse-focused')]", 2)
    # rellenar campo nombre pagina
    fu.get_path_sendkey("//input[contains(@class,'form-control ng-star-inserted')]", "Ver Usuarios", 1)
    # elegimos área de trabjo
    fu.get_path_click("(//span[contains(@class,'mat-button-toggle-label-content')])[1]", 1)
    # damos clic en aceptar o guardar
    fu.get_css_selector_click("button.btn-fancy", 1)
    test_drag_drop_table()


def test_drag_drop_table():
    elemento_mover = fu.selector_xpath("//img[@src='assets/images/widgets/table-widget.svg']")
    # ubicar la zona donde se soltará el elemento
    zona_soltar = fu.selector_css("app-page-slot")
    # crear una instancia de ActionChains
    acciones = ActionChains(driver=driver)
    time.sleep(1)
    # realizar la acción de arrastrar y soltar
    acciones.click_and_hold(elemento_mover)
    acciones.move_to_element(zona_soltar)
    acciones.release(zona_soltar)
    acciones.perform()
    time.sleep(2)
    # damos nombre al formulario
    fu.get_path_sendkey("//input[contains(@class,'form-control ng-star-inserted')]", "Usuarios", 1)
    # damos clic al selector
    fu.get_path_click("(//input[contains(@aria-autocomplete,'list')])[1]", 1)
    # seleccionamos data origin
    fu.get_path_click("(//div[contains(@role,'option')])[1]", 1)

    fu.get_path_click("(//input[contains(@aria-autocomplete,'list')])[2]", 1)
    fu.get_path_click("//div[contains(@class,'ng-option ng-option-marked ng-star-inserted')]", 1)
    # damos clic en crear
    fu.get_css_selector_click("button.accept", 1)
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
