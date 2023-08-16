class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad}"

    def __repr__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad}"

    def __add__(self, other):
        nueevo_valor = self.adad + other.adad


pedro = Persona("Pedro", 45)
print(pedro)