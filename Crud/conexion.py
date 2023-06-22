"""
En este archivo haremos la coneccion con la base de datos Crud
"""

import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable


class ConexionDB:
    # Datos de connexion:
    config = {
        'user': 'root',
        'password': 'admin123',
        'host': '192.168.10.47',
        'port': '3307',
        'database': 'crud'
    }

    def __init__(self):
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(**self.config)
            assert self.conexion, "Error no Conectado"
        except Error as e:
            print(f'Error al conectarse a la base de datos: {e}')

    def desconectar(self):
        if self.conexion.is_connected():
            self.conexion.close()
            # print('Desconexión exitosa de la base de datos')

    def ejecutar_consulta(self, consulta):
        cursor = self.conexion.cursor()
        try:
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            self.conexion.commit()
            return resultado
        except Error as e:
            self.conexion.rollback()
            print(f'Error al ejecutar la consulta: {e}')
        finally:
            cursor.close()

    def execute_sql_query(self, query):
        cursor = self.conexion.cursor()
        try:
            cursor.execute(query)
            if query.lower().startswith('select'):
                rows = cursor.fetchall()
                if len(rows) == 0:
                    print("No se encontraron resultados.")
                else:
                    columns = list(map(lambda x: x[0], cursor.description))
                    table = PrettyTable(columns)
                    for row in rows:
                        table.add_row(row)
                    print(table)
            else:
                self.conexion.commit()
                print("Consulta ejecutada exitosamente.")
        except Exception as e:
            print("Error al ejecutar la consulta:", e)
        finally:
            cursor.close()

