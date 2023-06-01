from selenium import webdriver

url = "https://appolow.app/#/auth/login"

# Configuración de opciones para el navegador Edge
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True

# Inicialización del driver de Selenium con las opciones de Edge
driver = webdriver.Edge(options=edge_options)

# Acceso a la URL
driver.get(url)

# Espera 10 segundos para que se cargue la página
driver.implicitly_wait(10)

# Cierre del navegador
driver.quit()
