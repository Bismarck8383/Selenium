import pandas as pd
from prettytable import PrettyTable

# Ejemplo de diccionario con datos de personas
datos_personas = {
    'nombre': ['Juan', 'María', 'Pedro', 'Laura'],
    'edad': [30, 25, 40, 35],
    'pais': ['España', 'México', 'Argentina', 'Chile']
}

# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(datos_personas)

# Crear una tabla con prettytable
tabla = PrettyTable()
tabla.field_names = df.columns

# Agregar filas a la tabla
for fila in df.itertuples(index=False):
    tabla.add_row(fila)

# Imprimir la tabla
print(tabla)
