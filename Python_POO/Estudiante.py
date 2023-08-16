class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return (
            f"Nombre: {self.name}\n"
            f"Edad: {self.age}"
        )


class Estudiante(Persona):
    def __init__(self, name, age, grado):
        super().__init__(name, age)
        self.grado = grado

    def info(self):
        return (
            f"Nombre: {self.name}\n"
            f"Edad: {self.age}\n"
            f"Grado: {self.grado}"
        )


estudent = Estudiante("Pedro", 25, 4)
info_student = estudent.info()
print(info_student)
