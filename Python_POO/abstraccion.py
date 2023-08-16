from abc import ABC, abstractmethod


class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def arrancar(self):
        pass

    @abstractmethod
    def detener(self):
        pass


class Coche(Vehiculo):
    def arrancar(self):
        return f"El coche {self.marca} {self.modelo} está arrancando."

    def detener(self):
        return f"El coche {self.marca} {self.modelo} se está deteniendo."


class Moto(Vehiculo):
    def arrancar(self):
        return f"La moto {self.marca} {self.modelo} está arrancando."

    def detener(self):
        return f"La moto {self.marca} {self.modelo} se está deteniendo."


# Crear instancias de Coche y Moto
coche = Coche(marca="Toyota", modelo="Corolla")
moto = Moto(marca="Honda", modelo="CBR")

# Usar los métodos de arranque y detención de los vehículos
print(coche.arrancar())
print(coche.detener())

print(moto.arrancar())
print(moto.detener())
