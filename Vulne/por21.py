import socket

# Dirección IP y puerto del servicio FTP
ip = "217.76.142.239"
port = 21

# Intento de conexión al servicio FTP
try:
    # Crear un socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar al servicio FTP
    s.connect((ip, port))

    # Recibir respuesta del servidor
    response = s.recv(1024).decode()

    print("Respuesta del servidor:", response)

    # Intento de autenticación débil
    s.send(b"USER anonymous\r\n")
    response = s.recv(1024).decode()
    print("Respuesta de autenticación:", response)

    # Cerrar la conexión
    s.close()

    if "230" in response:
        print("El servicio FTP es vulnerable a autenticación débil.")
    else:
        print("El servicio FTP no es vulnerable a autenticación débil.")

except socket.error as e:
    print("Error de conexión:", str(e))
