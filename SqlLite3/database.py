"""
Ejemplo de un crud con sqlite3
"""
import sqlite3
from prettytable import PrettyTable


class Usuarios:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                apellido TEXT,
                edad INTEGER,
                email TEXT
            )
        ''')
        self.conn.commit()

    def insert_data(self):
        print('### Ingrese los datos del nuevo cliente ###')
        nombre = input('Ingrese el nombre del cliente: ')
        while not nombre.isalpha():
            print('Error: el nombre solo puede contener letras')
            nombre = input('Ingrese el nombre del cliente: ')

        apellido = input('Ingrese el apellido del cliente: ')
        while not apellido.isalpha():
            print('Error: el apellido solo puede contener letras')
            apellido = input('Ingrese el apellido del cliente: ')

        edad = input('Ingrese la edad del cliente: ')
        while not edad.isdigit() or int(edad) < 0 or int(edad) > 115:
            print('Error: la edad solo puede contener números enteros positivos y no mayor a 115 años')
            edad = input('Ingrese la edad del cliente: ')

        email = input('Ingrese el email del cliente: ')
        while True:
            if not email:
                print('Error: el email no puede estar vacío')
                email = input('Ingrese el email del cliente: ')
            else:
                self.cursor.execute("SELECT * FROM clientes WHERE email = ?", (email,))
                resultado = self.cursor.fetchall()
                if len(resultado) > 0:
                    print('Error: el email ya está registrado')
                    email = input('Ingrese el email del cliente: ')
                else:
                    break

        self.cursor.execute('''
            INSERT INTO clientes (nombre, apellido, edad, email) VALUES (?, ?, ?, ?)
        ''', (nombre, apellido, edad, email))
        self.conn.commit()

        print('Cliente registrado exitosamente!')

    def display_data(self):
        self.cursor.execute('SELECT * FROM clientes')
        rows = self.cursor.fetchall()

        table = PrettyTable(["ID", "Nombre", "Apellido", "Edad", "Email"])

        for row in rows:
            table.add_row([row[0], row[1], row[2], row[3], row[4]])

        return table, len(rows)  # Devuelve la tabla y la cantidad de registros

    def update_data(self):
        while True:
            id = input('Ingrese el ID del cliente a actualizar: ')
            self.cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
            resultado = self.cursor.fetchall()
            if len(resultado) == 0:
                print('Error: el ID no existe. Ingrese un ID válido registrado')
            else:
                break

        print('### Ingrese los nuevos datos del cliente ###')
        nombre = input('Ingrese el nuevo nombre del cliente: ')
        while not nombre.isalpha():
            print('Error: el nombre solo puede contener letras')
            nombre = input('Ingrese el nuevo nombre del cliente: ')

        apellido = input('Ingrese el nuevo apellido del cliente: ')
        while not apellido.isalpha():
            print('Error: el apellido solo puede contener letras')
            apellido = input('Ingrese el nuevo apellido del cliente: ')

        edad = input('Ingrese la nueva edad del cliente: ')
        while not edad.isdigit() or int(edad) < 0 or int(edad) > 115:
            print('Error: la edad solo puede contener números enteros positivos y no mayor a 115 años')
            edad = input('Ingrese la nueva edad del cliente: ')

        email = input('Ingrese el nuevo email del cliente: ')
        while True:
            if not email:
                print('Error: el email no puede estar vacío')
                email = input('Ingrese el nuevo email del cliente: ')
            else:
                self.cursor.execute("SELECT * FROM clientes WHERE email = ? AND id != ?", (email, id))
                resultado = self.cursor.fetchall()
                if len(resultado) > 0:
                    print('Error: el email ya está registrado')
                    email = input('Ingrese el nuevo email del cliente: ')
                else:
                    break

        self.cursor.execute('''
            UPDATE clientes SET nombre = ?, apellido = ?, edad = ?, email = ? WHERE id = ?
        ''', (nombre, apellido, edad, email, id))
        self.conn.commit()

        print('Cliente actualizado exitosamente!')

    def delete_data(self):
        while True:
            id_cliente = input('Ingrese el ID del cliente a eliminar: ')
            if not id_cliente.isnumeric():
                print('Error: el ID solo puede contener números enteros positivos')
                continue

            self.cursor.execute('SELECT * FROM clientes WHERE id = ?', (id_cliente,))
            resultado = self.cursor.fetchone()

            if resultado is None:
                print('Error: el ID ingresado no corresponde a un cliente registrado')
            else:
                break

        self.cursor.execute('DELETE FROM clientes WHERE id = ?', (id_cliente,))
        self.conn.commit()
        print('Cliente eliminado exitosamente!')

    def close_connection(self):
        self.conn.close()

    def execute_sql_query(self, query):
        try:
            self.cursor.execute(query)
            if query.lower().startswith('select'):
                rows = self.cursor.fetchall()
                if len(rows) == 0:
                    print("No se encontraron resultados.")
                else:
                    columns = list(map(lambda x: x[0], self.cursor.description))
                    table = PrettyTable(columns)
                    for row in rows:
                        table.add_row(row)
                    print(table)
            else:
                self.conn.commit()
                print("Consulta ejecutada exitosamente.")
        except Exception as e:
            print("Error al ejecutar la consulta:", e)


usuarios_db = Usuarios("Usuarios.db")


def run_custom_query():
    while True:
        print("Escriba su consulta SQL (exit para salir):")
        query = input()
        if query.lower() == 'exit':
            break
        usuarios_db.execute_sql_query(query)


def menu_opciones():
    opciones = True

    while opciones:
        print("###### Menu Opciones ######")
        print("1. Lista Clientes")
        print("2. Registrar Clientes")
        print("3. Actualizar Clientes")
        print("4. Borrar Clientes")
        print("5. Ejecutar consulta SQL personalizada")
        print("6. Salir")
        opc = int(input("Selecciona un Opción : "))
        if 0 < opc < 7:
            if opc == 1:
                try:
                    table, reg = usuarios_db.display_data()
                    if reg > 0:
                        print(table)
                    else:
                        print("No hay clientes registrados")
                except:
                    print("No se pudo ejecutar la consulta")
            elif opc == 2:
                usuarios_db.insert_data()
            elif opc == 3:
                try:
                    table, reg = usuarios_db.display_data()
                    if reg > 0:
                        print(table)
                        usuarios_db.update_data()
                    else:
                        print("No hay cliente registrados para actualizar")
                except:
                    print("No se pudo ejecutar la consulta")

            elif opc == 4:
                try:
                    table, reg = usuarios_db.display_data()
                    if reg > 0:
                        print(table)
                        usuarios_db.delete_data()
                    else:
                        print("No hay cliente registrados para eliminar")
                except:
                    print("No se puede ejcutar la consulta")
            elif opc == 5:
                run_custom_query()
            elif opc == 6:
                print("saliendo ......")
                opciones = False
        else:
            print(f"El numero : {opc} no es valido, escriba del 1 al 6")


menu_opciones()
usuarios_db.close_connection()
