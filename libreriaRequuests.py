import requests

url = "https://parascrapear.com/"
user_agente ={"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
response = requests.get(url, headers=user_agente)
resultado  = response.status_code
cabezeras = response.headers
kookies = response.cookies
bien = response.ok
redireccionado = response.is_redirect
redirecpermanente = response.is_permanent_redirect
#respuestajson = response.json()
print(response.text)
print("----------------------------------------------")
print("EL resultado de estatus fue : ", resultado)
print("----------------------------------------------")
print("cabeceras de la llamada")
print(cabezeras)
print("----------------------------------------------")
print("se obtiene los cookies si los tuviera")
print(kookies)
print("----------------------------------------------")
print("se obtiene un booleano si fueramos redireccionado a otra zona ya sea una sola vez o permanente")
print("Resultado de redireccionado una vez : ", redireccionado)
print("Resultado de redireccionado permanentemente : ", redirecpermanente)
print("---------------------------------------------------------")
print("Obtenemos un JSON  de respuesta")
#print(respuestajson)
print("Obtenemos una URL  de respuesta")
print(response.request.url)
print("---------------")
print("Mostramos las cabeceras")
print(response.request.headers)
print("valor booleano enviado de status de conección {} ".format(bien))
print("----------------------------")
print("User Agent :  {}".format(user_agente))

#creamos un archivo html con la respuesta
with open("codigo_200.html", "w", encoding="utf-8") as f:
    f.write(response.text)

