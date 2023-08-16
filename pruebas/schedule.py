import schedule
import time


def mi_funcion():
    print("Esta es mi función que se ejecutará hoy a las 13:48.")


# Programar la ejecución de la función para hoy a las 13:48
schedule.every().day.at("13:48").do(mi_funcion)

# Mantener el script en ejecución para que la función se pueda ejecutar
while True:
    schedule.run_pending()
    time.sleep(1)
