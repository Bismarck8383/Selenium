class Coche:
    def __init__(self, marca, *colores, **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

    def arrancar(self):
        print(f"El coche {self.marca} avanza")

    def parar(self):
        print(f"EL coche : {self.marca} paro")

vehiculo = Coche("Seat", "Negro", "verde", md1=500, m2=300)
print(vehiculo.marca)
print(vehiculo.colores)
print(vehiculo.modelos)
print('------------------')
vehiculo.model = 400
print(f"El model es {vehiculo.model}")
vehiculo.arrancar()
vehiculo.parar()

vehiculo2 = Coche()

