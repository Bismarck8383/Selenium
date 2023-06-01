import requests
from bs4 import BeautifulSoup

url = "https://www.game.es/ACCESORIOS/AURICULARES/MULTI-PLATAFORMA/AURICULARES-TRUST-GXT310-GAMING-PS4-XONE-PC/125993"
user_agente = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
response = requests.get(url, headers=user_agente)
conectado = response.status_code

if conectado == 200:
    print("Estatus de coneccion : {}".format(conectado))
else:
    print("Error de Conección")

soup = BeautifulSoup(response.text, "html.parser")
titulo = soup.title
print("Titulo de la web :\n {} ".format(titulo.text))

span = soup.find_all(class_="title-tooltip")
for spa in span:
    print("Span seleccionado : {} ".format(spa.text))

print("-------------------------------------------------------")
div = soup.find("div", class_="thumb-title").find_all(class_="int")
for di in div:
    print("entero  :  {} ".format(di.text))

print("-------------------------------------------------------")

precios = soup.find_all(class_="int")
for pre in precios:
    print("Precios de articulo :  {} ".format(pre.text))

# tomar el enlace src
src = soup.find_all("img", class_="img-responsive")
for srcs in src:
    print("Los src : {}".format(srcs["src"]))

