class Animal:
    def hablar(self):
        pass


class Perro(Animal):
    def hablar(self):
        return "Woof!"


class Gato(Animal):
    def hablar(self):
        return "Meow!"


class Vaca(Animal):
    def hablar(self):
        return "Moo!"


# Función que hace que un animal hable independientemente de su tipo
def hacer_hablar(animal):
    return animal.hablar()


# Crear instancias de diferentes animales
perro = Perro()
gato = Gato()
vaca = Vaca()

# Hacer que los animales hablen
print(hacer_hablar(perro))  # Salida: Woof!
print(hacer_hablar(gato))  # Salida: Meow!
print(hacer_hablar(vaca))  # Salida: Moo!
