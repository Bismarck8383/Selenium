class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def inicial(self):
        print("Metodo desde Clase padre persona")


class Empleado(Persona):
    def __init__(self, nombre, edad, ciudad, email, telefono, cargo=None):
        super().__init__(nombre, edad, ciudad)
        self.email = email
        self.telefono = telefono
        self.cargo = cargo

    def info_empleado(self):
        return (
            f"El empleado: {self.nombre}\n"
            f"Edad: {self.edad}\n"
            f"Ciudad: {self.ciudad}\n"
            f"Email: {self.email}\n"
            f"Teléfono: {self.telefono}\n"
            f"Cargo: {self.cargo}"
        )

    def inicial(self):
        print("Saludando desde la clase Empleado")


class Cliente(Empleado):
    def __init__(self, nombre, edad, ciudad, email, telefono, estado):
        super().__init__(nombre, edad, ciudad, email, telefono, cargo=None)
        self.estado = estado

    def info_empleado(self):
        empleado_info = super().info_empleado()
        return f"{empleado_info}\nEstado: {self.estado}"


class Personal(Empleado):
    pass


# Crear un objeto Cliente
cliente1 = Cliente(
    nombre="María",
    edad=25,
    ciudad="Buenos Aires",
    email="maria@example.com",
    telefono="987654321",
    estado="Activo"
)

# Imprimir información del cliente con estado
print(cliente1.info_empleado())

# Crear un objeto Empleado
empleado1 = Empleado(
    nombre="Juan",
    edad=30,
    ciudad="Ciudad de México",
    email="juan@example.com",
    telefono="123456789",
    cargo="Contable"
)

# Imprimir información del empleado con saltos de línea
print(empleado1.info_empleado())
personal = Personal("Alberto", 45, "cadaques", "correo@correo.com", 698532147, "Recurso Humanos")
print(f"El Nuevo personal es  : {personal.nombre} de {personal.edad} años")
print(empleado1.inicial())
