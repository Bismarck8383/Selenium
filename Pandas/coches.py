import pandas as pd
from prettytable import PrettyTable
import numpy as np

columnas = ["Marca", "Precio", "disponibilidad", "año"]

cocheA = ["Seat", 10e3, True, 2020]
cocheB = ["Fiat", 9e3, False, 2022]

df = pd.DataFrame([cocheA, cocheB], columns=columnas)


# Función para transformar True en "disponible" y False en "no disponible"
def transformar_disponibilidad(valor):
    return "disponible" if valor else "no disponible"


# Aplicar la función a la columna "disponibilidad"
df["disponibilidad"] = df["disponibilidad"].apply(transformar_disponibilidad)

# Crear la tabla con prettytable
tabla = PrettyTable()
tabla.field_names = df.columns

# Agregar filas a la tabla
for fila in df.itertuples(index=False):
    tabla.add_row(fila)

print(df)
print("--------------------")
print(tabla)
d = {'a': 1, 'b': 2, 'c': 3}
ser = pd.Series(data=d, index=['a', 'b', 'c'])
print(ser)
print("--------------------")

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df2)
