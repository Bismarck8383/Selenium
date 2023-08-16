# Definir un decorador
def decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de llamar a la función")
        resultado = func(*args, **kwargs)
        print("Después de llamar a la función")
        return resultado

    return wrapper


# Aplicar el decorador a una función
@decorador
def saludar(nombre):
    return f"Hola, {nombre}!"


# Llamar a la función decorada
mensaje = saludar("Juan")
print(mensaje)
