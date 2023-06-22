import requests

url = 'https://avatar-bismarck.appolow.app/api/keycloak/auth/token'
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'es-ES,es;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://avatar-bismarck.appolow.app',
    'Referer': 'https://avatar-bismarck.appolow.app/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                  'Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}
data = {
    'username': 'admin',
    'password': 'admin'
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    token = response.json()['access_token']
    with open('token_file.txt', 'w') as f:
        f.write(token)
    print('Token de acceso obtenido y guardado correctamente.')
else:
    print('Error al obtener el token de acceso:', response.text)
