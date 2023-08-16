class Miclase:
    def __init__(self, name, valor, pswd):
        self._name = name
        # atributo privado
        self._atributo_privado = valor
        # atributo muy privado
        self.__muy_privado = pswd

    # Metodo para acceder al atributo privado
    def get_privado(self):
        return self._atributo_privado

    # Método para acceder al atributo muy privado
    def get_muy_privado(self):
        return self.__muy_privado

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def set_muy_privado(self, new_muy_privado):
        self.__muy_privado = new_muy_privado


# Crear un objeto de Miclase
objeto = Miclase(name="pedro", valor=5, pswd="admin1234")

# Acceder a los atributos
print(f"Nombre: {objeto.get_name()}")
print(f"Valor privado: {objeto.get_privado()}")

# Acceder al atributo muy privado utilizando el método
print(f"Atributo muy privado: {objeto.get_muy_privado()}")

# Cambiamos el nombre accediento al metodo privado
objeto.set_name("Manolo")
print(f"New name : {objeto.get_name()}")

# cambiamos datos del muy privado
objeto.set_muy_privado("mosnter¡123")
print(f"Nueva Contraseña: {objeto.get_muy_privado()}")
