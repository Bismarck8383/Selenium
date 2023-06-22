#!/bin/bash

# Pide al usuario el token Bearer
#echo "Introduzca el token Bearer:"
#read token

# Lee el token Bearer del archivo
token=$(cat token_file.txt)

# Usa el token en la solicitud curl
curl 'https://avatar-bismarck.appolow.app/api/views/view84778995datosclienteslistadoclientes/search?sort=ASC&sortField=id&page=0&size=20&semantic=&search=' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-ES,es;q=0.9' \
  -H "Authorization: Bearer $token" \
  -H 'Connection: keep-alive' \
  -H 'Referer: https://avatar-bismarck.appolow.app/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --compressed > clientes.json
