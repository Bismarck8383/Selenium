class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


class Revista:
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria


class Usuario(Persona, Libro):
    def __init__(self, nombre, edad, titulo, autor):
        Persona.__init__(self, nombre, edad)
        Libro.__init__(self, titulo, autor)


class Suscriptor(Persona, Revista):
    def __init__(self, nombre, edad, nombre_revista, categoria):
        Persona.__init__(self, nombre, edad)
        Revista.__init__(self, nombre_revista, categoria)


# Crear un usuario que escribe libros
autor = Usuario(nombre="Juan", edad=30, titulo="Programación en Python", autor="Juan Pérez")
print(f"{autor.nombre} es el autor del libro '{autor.titulo}' por {autor.autor}")

# Crear un suscriptor de una revista
suscriptor = Suscriptor(nombre="María", edad=25, nombre_revista="Tech Magazine", categoria="Tecnología")
print(f"{suscriptor.nombre} es suscriptor de la revista '{suscriptor.nombre}' en la categoría {suscriptor.categoria}")
