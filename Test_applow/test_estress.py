import requests
import random
import string

url = "https://delivery-appolow.appolow.app/api/views/view15279508nuevoclientecrearcliente"
tenant_id = "5d3d06ca-f764-4afc-a238-07e84df62038"

headers = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJnOTRrWE43eDc0a1Fpa0RYa2hQeFdRakJvY3VId3hwVlozMFk0dGlzWUVJIn0.eyJleHAiOjE2ODQxNzEwMzQsImlhdCI6MTY4NDEzNTAzNCwianRpIjoiZjVlNGQ3NjktODMxOC00YTY4LTg1MjMtY2NlZGJhZGUzODRmIiwiaXNzIjoiaHR0cHM6Ly9hdXRoMDEuYXBwb2xvdy5hcHAvYXV0aC9yZWFsbXMvZGVsaXZlcnkiLCJhdWQiOlsicmVhbG0tbWFuYWdlbWVudCIsImFjY291bnQiXSwic3ViIjoiZjQ3MGE3NzEtM2E2Ni00NmNkLThhMWQtNmUyNzJkMTgwZjQxIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiZGVsaXZlcnktY2xpIiwic2Vzc2lvbl9zdGF0ZSI6IjdkNGMxYTlkLWI0ZTMtNDJhMC04YWU5LTQ0YTM3NzgwODk0NyIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJST0xFX0FETUlOIiwiZGVmYXVsdC1yb2xlcy1kZWxpdmVyeSIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsicmVhbG0tbWFuYWdlbWVudCI6eyJyb2xlcyI6WyJ2aWV3LXJlYWxtIiwidmlldy1pZGVudGl0eS1wcm92aWRlcnMiLCJtYW5hZ2UtaWRlbnRpdHktcHJvdmlkZXJzIiwiaW1wZXJzb25hdGlvbiIsInJlYWxtLWFkbWluIiwiY3JlYXRlLWNsaWVudCIsIm1hbmFnZS11c2VycyIsInF1ZXJ5LXJlYWxtcyIsInZpZXctYXV0aG9yaXphdGlvbiIsInF1ZXJ5LWNsaWVudHMiLCJxdWVyeS11c2VycyIsIm1hbmFnZS1ldmVudHMiLCJtYW5hZ2UtcmVhbG0iLCJ2aWV3LWV2ZW50cyIsInZpZXctdXNlcnMiLCJ2aWV3LWNsaWVudHMiLCJtYW5hZ2UtYXV0aG9yaXphdGlvbiIsIm1hbmFnZS1jbGllbnRzIiwicXVlcnktZ3JvdXBzIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJzaWQiOiI3ZDRjMWE5ZC1iNGUzLTQyYTAtOGFlOS00NGEzNzc4MDg5NDciLCJ0ZW5hbnRzIjpbImFwcG9sb3ciXSwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJuYW1lIjoiYWRtaW4gYWRtaW4iLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJhZG1pbiIsImdpdmVuX25hbWUiOiJhZG1pbiIsImZhbWlseV9uYW1lIjoiYWRtaW4iLCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.SoWt58vHliohTGEt7zLrBD1VdEQEzjEqQexRkoV1Ykts6VR_ER8ZapGuTn5zAkIbE_1AY7YjYKpBJam817lQ-q9sGdFsWDRJIfWGeL_nFn8OMcuvzbQsuqS5Rmjt-a37YQ9ZKrXUP6NynUNsS1zbCeF3Smi8Wrk5kXD_YPTXgFNF27yUQbJgH7Ag0JuJkvf38VU058VkD8JzwnnsVhVUG-bbYEAXbqWAU5dfR2Yo5kkEgo4oHnhMYpWU9-A6xyU3oc3ukWiJJFUd2uJ0Ntl_2kK0-Z6_-yL-CkXnvgtehcX6zjF0ZeklvvGkcOBYI99g4koxenRv6IMVxxyOBxLhug"

}

data = {
    "tenantId": tenant_id,
    "registros": []
}

num_records = 20
start_id = 268


def generate_random_email():
    random_str = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{random_str}@correo.com"


for i in range(num_records):
    telefono = random.randint(10000000, 99999999)
    email = generate_random_email()

    record = {
        "id": start_id + i,
        "tenantId": tenant_id,
        "nombre": f"Nombre {i + 1}",
        "direccion": f"Dirección {i + 1}",
        "Email": email,
        "telefono": str(telefono),
        "email": email
    }
    data["registros"].append(record)

params = {
    "tenantId": tenant_id
}

response = requests.post(url, json=data, headers=headers, params=params)

if response.status_code == 200:
    print("Datos enviados correctamente.")
else:
    print("Error al enviar los datos:", response.status_code, response.text)
