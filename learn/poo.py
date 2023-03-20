class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b

    def potencia(self, a, b):
        return a ** b

    def raiz_cuadrada(self, a):
        if a < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        return a ** 0.5


mi_calculadora = Calculadora()

print(mi_calculadora.suma(2, 3))  # Imprime 5
print(mi_calculadora.resta(5, 2))  # Imprime 3
print(mi_calculadora.multiplicacion(2, 4))  # Imprime 8
print(mi_calculadora.division(10, 2))  # Imprime 5.0
print(mi_calculadora.potencia(2, 3))  # Imprime 8
print(mi_calculadora.raiz_cuadrada(9))  # Imprime 3.0
