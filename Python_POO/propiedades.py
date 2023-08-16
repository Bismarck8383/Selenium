class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre.capitalize()

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("La edad no puede ser negativa")

    @nombre.deleter
    def nombre(self):
        del self.nombre


# Crear un objeto de Persona
persona = Persona(nombre="Juan", edad=30)

# Obtener nombre y edad
print(f"Nombre: {persona.nombre}")
print(f"Edad: {persona.edad}")

# Cambiar nombre y edad
persona.nombre = "María"
persona.edad = 25
print("--------------------------------------")
# Obtener nombre y edad actualizados
print(f"Nombre: {persona.nombre}")
print(f"Edad: {persona.edad}")
