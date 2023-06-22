#!/bin/bash

response=$(curl -s 'https://avatar-bismarck.appolow.app/api/keycloak/auth/token' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-ES,es;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://avatar-bismarck.appolow.app' \
  -H 'Referer: https://avatar-bismarck.appolow.app/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"username":"admin","password":"admin"}' \
  --compressed)

# Supongamos que el token se encuentra en una propiedad llamada 'token' en la respuesta JSON
token=$(echo $response | jq -r '.token')

echo $token
