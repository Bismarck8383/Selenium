import os
import platform
import subprocess

# Obtener el directorio actual
directorio_actual = os.getcwd()

# Configurar el servidor web HTTP de Python en el puerto 80
os.system("python -m http.server 80")

# Programar la ejecución del script en el arranque del sistema operativo
if platform.system() == "Windows":
    # En Windows, crear una tarea programada utilizando el Programador de tareas
    ruta_script = os.path.join(directorio_actual, "servidor.py")
    comando = f'schtasks /create /tn "Servidor web" /sc onstart /tr "{ruta_script}"'
    subprocess.run(comando, shell=True)

elif platform.system() == "Linux" or platform.system() == "Darwin":
    # En sistemas Unix, agregar una línea al archivo /etc/rc.local para ejecutar el script
    ruta_script = os.path.join(directorio_actual, "servidor.py")
    linea_rclocal = f"/usr/bin/python {ruta_script} &"
    with open("/etc/rc.local", "a") as rclocal:
        rclocal.write(linea_rclocal)

