# Abre el archivo en modo de escritura. Si existe, se sobrescribe. Si no existe, se crea.
with open('clientes.json', 'w') as file:
    # Aquí puedes escribir en el archivo. Por ahora, lo dejamos vacío.
    pass
import os
import requests

# Abre el archivo en modo de escritura. Si existe, se sobrescribe. Si no existe, se crea.
with open('clientes.json', 'w') as file:
    # Aquí puedes escribir en el archivo. Por ahora, lo dejamos vacío.
    pass
# Leer el token Bearer del archivo
with open('token_file.txt', 'r') as file:
    token = file.read().strip()


# URL para la solicitud
url = 'https://avatar-bismarck.appolow.app/api/views/view84778995datosclienteslistadoclientes/search?sort=ASC&sortField=id&page=0&size=50&semantic=&search='

# Definir los headers para la solicitud
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'es-ES,es;q=0.9',
    'Authorization': f'Bearer {token}',
    'Connection': 'keep-alive',
    'Referer': 'https://avatar-bismarck.appolow.app/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# Realizar la solicitud
response = requests.get(url, headers=headers)


# Verificar si la solicitud fue exitosa
if response.status_code == 200:

    print(f"datos Obtenidos correctamente Code :{response.status_code}")
    # Si el archivo 'clientes.json' no existe, lo crea
    if not os.path.isfile('clientes.json'):
        with open('clientes.json', 'w') as file:
            pass

    # Escribir el contenido de la respuesta en 'clientes.json'
    with open('clientes.json', 'w') as file:
        file.write(response.text)
else:
    print(f"Error: Received status code {response.status_code}")
