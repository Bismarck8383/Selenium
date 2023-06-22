import pymysql
import json
import sys
from prettytable import PrettyTable

config = {
    'user': 'root',
    'password': 'admin123',
    'host': '192.168.10.47',
    'port': 3307,
    'database': 'bash'
}

# Carga los datos del archivo JSON
with open('clientes.json') as f:
    data = json.load(f)

# Inicializa una tabla PrettyTable
table = PrettyTable()
table.field_names = ["ID", "Nombre", "Edad", "Tenant ID"]

# Establece la conexión a la base de datos
try:
    connection = pymysql.connect(**config)
except pymysql.MySQLError as e:
    print(f"Error al conectar a la base de datos: {e}")
    sys.exit()

try:
    with connection.cursor() as cursor:
        # Recorre los elementos en los datos
        for item in data['content']:
            # Comprueba si el id ya existe en la base de datos
            sql_check = "SELECT * FROM cliente WHERE id = %s"
            cursor.execute(sql_check, (item['id'],))
            result = cursor.fetchone()

            # Si el id no existe, inserta los datos
            if result is None:
                try:
                    sql_insert = "INSERT INTO cliente (id, nombre, edad, tenantId) VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql_insert, (item['id'], item['nombre'], item['edad'], item['tenantId']))
                except pymysql.MySQLError as e:
                    print(f"Error al insertar datos: {e}")
            else:
                # print(f"El ID {item['id']} ya existe en la base de datos. No se insertará el registro.")

                # Agrega las filas a la tabla PrettyTable
                table.add_row([item['id'], item['nombre'], item['edad'], item['tenantId']])

    # Se debe llamar a connection.commit() para que los cambios se guarden en la base de datos
    connection.commit()
    print("Los datos se han insertado correctamente.")
except Exception as e:
    print(f"Error Algo salio mal: {e}")
finally:
    connection.close()

# Imprime la tabla de datos no insertados
print("\nDatos no insertados (ID ya existentes):")
print(table)
