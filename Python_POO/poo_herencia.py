class Carro:
    def __init__(self, nom, mod, color, precio):
        self.nombre = nom
        self.modelo = mod
        self.color = color
        self.precio = precio

    def description(self):
        print(f"Nombre : {self.nombre} \n Modelo : {self.modelo}\n Color : {self.color} \n Precio : {self.precio} ")


class Cochazo(Carro):
    def __init__(self, nom, mod, color, precio, motor):
        super().__init__(nom, mod, color, precio)
        self.motor = motor

    def description(self):
        print(
            f"Nombre : {self.nombre} \n Modelo : {self.modelo}\n Color : {self.color} \n Precio : {self.precio}\n Motor : {self.motor} ")


class Autobuses(Carro):
    def __init__(self, nom, mod, color, precio, motor, tn):
        super().__init__(nom, mod, color, precio)
        self.motor = motor
        self.tn = tn

    def description(self):
        print(
            f"Nombre : {self.nombre} \n Modelo : {self.modelo}\n Color : {self.color} \n Precio : {self.precio}\n Motor : {self.motor}\n TN : {self.tn} ")


iveco = [
    ("flota", "1998", "Rojo", 42355, 12000, 40),
    ("Mini", "2001", "verde", 33355, 11000, 25)
]

seat = [
    Cochazo("Ibiza", "1998", "Rojo", 12355, 1200),
    Cochazo("Toledo", "2005", "Verde", 18000, 1600),
    Cochazo("Leon", "2009", "Negro", 22500, 1800)
]

susuki = [
    Cochazo("Swift", "1999", "Rojo", 12355, 1200),
    Cochazo("Baleen", "2018", "Verde", 18000, 1600),
    Cochazo("Kisashi", "2002", "Negro", 22500, 1800)
]
for coches in seat:
    coches.description()
    print("-----------------------------")

for coches in susuki:
    coches.description()
    print("------------------------------")

autobuses = []
for nom, mod, color, precio, motor, tn in iveco:
    big = Autobuses(nom, mod, color, precio, motor, tn)
    autobuses.append(big)
for bus in autobuses:
    bus.description()