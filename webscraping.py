import requests
from bs4 import BeautifulSoup

url = "https://parascrapear.com/"

# Hacer la solicitud a la página web
response = requests.get(url)

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

limite = int(input("Introduce limite a mostrar : "))
autores = sopa.find_all(class_="author", limit=limite)
for p in autores:
    print("Author : {}".format(p.text))