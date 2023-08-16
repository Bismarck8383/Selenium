import re

import requests
from bs4 import BeautifulSoup

url = "https://parascrapear.com/"

cookiess = cookies = {"micookie": "valor del mio"}

# Hacer la solicitud a la página web
response = requests.get(url, cookies=cookies)

# cabeceras
print("--------------------------------------------")
#print(response.headers)

cookies = response.cookies
for cookie in cookies:
    print(f"Nombre_cookies : {cookie.name},\n Valor :  {cookie.value}")

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Analizar el HTML de la página
    soup = BeautifulSoup(response.text, "html.parser")

    # Extraer la información que deseas
    title = soup.find("title").text
    print("Título de la página:", title)

else:
    print("No se pudo acceder a la página")

sopa = BeautifulSoup(response.text, "html.parser")

# Solicitar al usuario la letra por la que desea filtrar los autores
letra = input("Introduce la letra mayuscula por la que quieres filtrar los autores: ")

# Construir la expresión regular para buscar autores por la letra especificada
regex = "^" + letra

limite = int(input("Introduce cantidad de autores a mostrar : "))
autores = sopa.find_all(class_="author", string=re.compile(regex), limit=limite)
# Imprimir los autores encontrados o un mensaje de error si no se encontraron
if len(autores) > 0:
    for p in autores:
        print("Author : {}".format(p.text))
else:
    print("No se encontraron autores que comiencen con la letra", letra)
