class Telefono:
    def __init__(self, color, precio):
        self.color = color
        self.precio = precio

    def enviar_sms(self, mensaje):
        return f"Mensaje enviado: {mensaje}"

    def llamar(self, numero):
        return f"El número marcado es: {numero}"

    def __del__(self):
        print("El objeto ha sido destruido")


class IBMTel(Telefono):
    def usar_ibm_software(self):
        return "Usando software exclusivo de IBM."

    def __str__(self):
        return f"Teléfono IBM de color {self.color}"

    def ver_precio(self):
        return f"El precio es {self.precio}"


class AppleTel(Telefono):
    def usar_siri(self):
        return "Hola, soy Siri. ¿En qué puedo ayudarte?"

    def __str__(self):
        return f"Teléfono Apple de color {self.color}"

    def ver_precio(self):
        return f"El precio es {self.precio}"


class SamsungTel(Telefono):
    def usar_bixby(self):
        return "Hola, soy Bixby. ¿Cómo puedo asistirte?"

    def ver_precio(self):
        return f"El precio es {self.precio}"

    def __str__(self):
        return f"Teléfono samsung de color {self.color}"


# Ejemplo de uso:

# Crear un teléfono de IBM
ibm_telefono = IBMTel(color="negro", precio=1250)
print(ibm_telefono.usar_ibm_software())
print(ibm_telefono.enviar_sms("Hola desde IBM!"))
print(ibm_telefono)
print(ibm_telefono.ver_precio())

# Crear un teléfono de Apple
apple_telefono = AppleTel(color="blanco", precio=1320)
print(apple_telefono.usar_siri())
print(apple_telefono.llamar(123456789))
print(apple_telefono)
print(apple_telefono.ver_precio())

# Crear un teléfono de Samsung
samsung_telefono = SamsungTel(color="azul", precio=854)
print(samsung_telefono.usar_bixby())
print(samsung_telefono.enviar_sms("¡Hola desde Samsung!"))
print(samsung_telefono)
