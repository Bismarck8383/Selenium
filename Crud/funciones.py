from datetime import datetime

from conexion import ConexionDB
from prettytable import PrettyTable


def mostrar_clientes():
    # Crea una instancia de ConexionDB y se conecta a la base de datos
    conexion = ConexionDB()
    conexion.conectar()

    # Ejecuta una consulta para seleccionar todos los clientes y lee los resultados
    consulta = 'SELECT * FROM cliente ORDER BY id ASC'
    resultados = conexion.ejecutar_consulta(consulta)

    # Creamos la tabla
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'Nombre', 'Apellido', 'Edad', 'Email', 'Fecha registro', 'Ciudad']

    # Muestra los resultados en la consola
    print('####### Clientes registrados: ##########')
    for fila in resultados:
        tabla.add_row([fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]])

        """
        print(f'ID: {fila[0]}')
        print(f'Nombre: {fila[1]}')
        print(f'Apellido: {fila[2]}')
        print(f'Edad: {fila[3]}')
        print(f'Email: {fila[4]}')
        print(f'Fecha de Nacimiento: {fila[5]}')
        print(f'Ciudad: {fila[6]}')
        print('--------------------------')
        """
    # mostramos la tabla
    print(tabla)
    conexion.desconectar()


def crear_cliente():
    # Pedir datos del cliente
    print("### Rellene todos los datos del cliente ###")
    nombre = input('Ingrese el nombre del cliente: ')
    while not nombre.isalpha():
        print('Error: el nombre solo puede contener letras')
        nombre = input('Ingrese el nombre del cliente: ')

    apellido = input('Ingrese el apellido del cliente: ')
    while not apellido.isalpha():
        print('Error: el apellido solo puede contener letras')
        apellido = input('Ingrese el apellido del cliente: ')

    edad = input('Ingrese la edad del cliente: ')
    while not edad.isnumeric() or int(edad) < 0 or int(edad) > 115:
        print('Error: la edad solo puede contener números enteros positivos y no mayor a 115 años')
        edad = input('Ingrese la edad del cliente: ')

    email = input('Ingrese el email del cliente: ')
    while True:
        if not email:
            print('Error: el email no puede estar vacío')
            email = input('Ingrese el email del cliente: ')
        else:
            conexion = ConexionDB()
            conexion.conectar()
            consulta = f"SELECT * FROM cliente WHERE email = '{email}'"
            resultado = conexion.ejecutar_consulta(consulta)
            conexion.desconectar()
            if len(resultado) > 0:
                print('Error: el email ya está registrado')
                email = input('Ingrese el email del cliente: ')
            else:
                break

    while True:
        fecha_reg = input('Ingrese la fecha de registro del cliente (formato AAAA-MM-DD): ')
        try:
            fecha_reg = datetime.strptime(fecha_reg, '%Y-%m-%d')

            break
        except ValueError:
            print('Error: formato de fecha inválido. Intente de nuevo.')

    ciudad = input('Ingrese la ciudad del cliente: ')
    while not ciudad.isalpha():
        print('Error: la ciudad solo puede contener letras')
        ciudad = input('Ingrese la ciudad del cliente: ')

    # Conectar a la base de datos
    conexion = ConexionDB()
    conexion.conectar()

    # Insertar nuevo cliente
    consulta = f"INSERT INTO cliente(nombre, apellido, edad, email, fecha_reg, ciudad) " \
               f"VALUES('{nombre}', '{apellido}', {edad}, '{email}', '{fecha_reg}', '{ciudad}')"
    conexion.ejecutar_consulta(consulta)

    print('Cliente registrado exitosamente!')
    # Desconectar de la base de datos
    conexion.desconectar()


def update_clientes():
    # Pedir el ID del cliente a actualizar
    while True:
        id_cliente = input('Ingrese el ID del cliente a actualizar: ')
        conexion = ConexionDB()
        conexion.conectar()
        consulta = f"SELECT * FROM cliente WHERE id = {id_cliente}"
        resultado = conexion.ejecutar_consulta(consulta)
        conexion.desconectar()
        if len(resultado) == 0:
            print('Error: el ID no existe. Ingrese un ID válido registrado')
        else:
            break

    # Pedir datos actualizados del cliente
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
    while not edad.isnumeric() or int(edad) < 0 or int(edad) > 115:
        print('Error: la edad solo puede contener números enteros positivos y no mayor a 115 años')
        edad = input('Ingrese la nueva edad del cliente: ')

    email = input('Ingrese el nuevo email del cliente: ')
    while True:
        if not email:
            print('Error: el email no puede estar vacío')
            email = input('Ingrese el nuevo email del cliente: ')
        else:
            conexion = ConexionDB()
            conexion.conectar()
            consulta = f"SELECT * FROM cliente WHERE email = '{email}'"
            resultado = conexion.ejecutar_consulta(consulta)
            conexion.desconectar()
            if len(resultado) > 0:
                print('Error: el email ya está registrado')
                email = input('Ingrese el nuevo email del cliente: ')
            else:
                break

    while True:
        fecha_reg = input('Ingrese la nueva fecha de registro del cliente (formato AAAA-MM-DD): ')
        try:
            fecha_reg = datetime.strptime(fecha_reg, '%Y-%m-%d')
            break
        except ValueError:
            print('Error: formato de fecha inválido. Intente de nuevo.')

    ciudad = input('Ingrese la nueva ciudad del cliente: ')
    while not ciudad.isalpha():
        print('Error: la ciudad solo puede contener letras')
        ciudad = input('Ingrese la nueva ciudad del cliente: ')

    # Conectar a la base de datos
    conexion = ConexionDB()
    conexion.conectar()

    # Actualizar cliente
    consulta = f"UPDATE cliente SET nombre = '{nombre}', apellido = '{apellido}', " \
               f"edad = {edad}, email = '{email}', fecha_reg = '{fecha_reg}', " \
               f"ciudad = '{ciudad}' WHERE id = {id_cliente}"
    conexion.ejecutar_consulta(consulta)

    print('Cliente actualizado exitosamente!')
    # Desconectar de la base de datos
    conexion.desconectar()


def eliminar_cliente():
    # Pedir id del cliente
    while True:
        id_cliente = input('Ingrese el id del cliente a eliminar: ')
        if not id_cliente.isnumeric():
            print('Error: el id solo puede contener números enteros')
            continue

        conexion = ConexionDB()
        conexion.conectar()
        consulta = f"SELECT * FROM cliente WHERE id = {id_cliente}"
        resultado = conexion.ejecutar_consulta(consulta)
        conexion.desconectar()

        if len(resultado) == 0:
            print('Error: el id ingresado no corresponde a un cliente registrado')
        else:
            break

    # Conectar a la base de datos
    conexion = ConexionDB()
    conexion.conectar()

    # Eliminar cliente
    consulta = f"DELETE FROM cliente WHERE id = {id_cliente}"
    conexion.ejecutar_consulta(consulta)

    print('Cliente eliminado exitosamente!')
    # Desconectar de la base de datos
    conexion.desconectar()





