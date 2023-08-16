import requests

url = 'https://appolow.app/#/auth/login'
data = {'username': 'appolow', 'password': '44o548gakw'}

headers = {
    'Cache-Control': 'no-cache',
    'Content_type': 'aplication/x-www-form-urlencoded'
}
response = requests.post(url, headers=headers, data=data)

resultado = response.status_code
if resultado == 200:
    print('Login successful! status : ', resultado)
else:
    print('Login failed. status : ', resultado)
