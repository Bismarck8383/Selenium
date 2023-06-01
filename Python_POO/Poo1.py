"""
Ejemplo de un relog digital

"""
import datetime
import time


class tiempo:
    def __init__(self):
        self.hora = 0
        self.minutos = 0
        self.segundos = 0

    def actualizar(self):
        ahora = datetime.datetime.now()
        self.hora = ahora.hour
        self.minutos = ahora.minute
        self.segundos = ahora.second

    def imprimir(self):
        # formato:02 en la función imprimir para garantizar que los valores de hora,
        # @minutos y segundos siempre tengan dos dígitos, incluyendo ceros a la izquierda si es necesario.
        return f"H :{self.hora:02} M :{self.minutos:02} S : {self.segundos:02}"


reloj = tiempo()

while True:
    reloj.actualizar()
    print(reloj.imprimir(), end='\r', flush=True)
    time.sleep(0.001)
