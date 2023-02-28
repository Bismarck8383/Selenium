from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from funciones.selenium_funciones import FuncionesGlobales
from selenium.webdriver import ActionChains
import time


def drag_drop():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    f = FuncionesGlobales(driver=driver)
    f.navigate_to("https://testpages.herokuapp.com/styled/drag-drop-javascript.html")

    time.sleep(2)
    # ubicar el elemento que se moverá
    elemento_mover = f.selector_xpath("(//p[contains(.,'Drag me')])[1]")

    # ubicar la zona donde se soltará el elemento
    zona_soltar = f.selector_xpath("//div[contains(@id,'droppable1')]")
    zona_2 = f.selector_xpath("//div[contains(@id,'droppable2')]")

    # crear una instancia de ActionChains
    acciones = ActionChains(driver=driver)

    # realizar la acción de arrastrar y soltar
    # acciones.drag_and_drop(elemento_mover, zona_soltar)
    acciones.click_and_hold(elemento_mover)
    acciones.move_to_element(zona_soltar)
    acciones.release(zona_soltar)
    acciones.perform()
    time.sleep(3)
    acciones.drag_and_drop(elemento_mover, zona_2)

    acciones.perform()
    time.sleep(5)


drag_drop()
