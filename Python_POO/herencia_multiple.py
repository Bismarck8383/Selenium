class Persona:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def info(self):
        return f"La persona {self.name} de {self.age} años vive en {self.city}"


class Deporte:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_hablidad(self):
        return f"Su habilidad es {self.habilidad}"


class Deportista(Persona, Deporte):
    def __init__(self, name, age, city, habilidad, salario, equipo):
        Persona.__init__(self, name, age, city)
        Deporte.__init__(self, habilidad)
        self.salario = salario
        self.equipo = equipo

    def info_deportista(self):
        return (
            f"Don {self.name}\n"
            f"de {self.age} años \n"
            f"de la Ciudad de {self.city}\n"
            f"Tiene la habilidad de {self.habilidad}\n"
            f"tiene un salario de {self.salario} Euros\n"
            f"Compite en el equipo de {self.equipo}"
        )


deportista = Deportista("Carlos", 25, "Malaga", "Ciclista", 2500, "Movistar")

print(deportista.info_deportista())
# verificamos si una clase hereda de otra
hereda = issubclass(Deportista, Deporte)
print(hereda)
