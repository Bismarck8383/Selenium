from conexion import ConexionDB
import conexion
import funciones


def run_custom_query(conexion):
    while True:
        print("Escriba su consulta SQL (exit para salir):")
        query = input()
        if query.lower() == 'exit':
            break
        conexion.execute_sql_query(query)


def menu_opciones():
    conectar = ConexionDB()
    conectar.conectar()
    # query que trae todos los clientes
    query = 'SELECT * FROM cliente'
    clientes = conectar.ejecutar_consulta(query)
    opciones = True
    while opciones:
        print("######Menu Opciones#######")
        print("1. Lista Clientes")
        print("2. Registrar Clientes")
        print("3. Actualizar Clientes")
        print("4. Borrar Clientes")
        print("5. Ejecutar consulta personalizada")
        print("6. Salir")

        opc = int(input("Selecciona un Opción : "))
        if 0 < opc < 7:
            if opc == 1:
                try:
                    if len(clientes) > 0:
                        funciones.mostrar_clientes()
                    else:
                        print("No hay clientes registrados")
                except:
                    print("No se pudo ejecutar la consulta")
            elif opc == 2:
                funciones.crear_cliente()
            elif opc == 3:
                try:
                    if len(clientes) > 0:
                        funciones.mostrar_clientes()
                        funciones.update_clientes()
                    else:
                        print("no hay Clientes registrados")
                except:
                    print("No se pudo ejecutar la consulta")
            elif opc == 4:
                try:
                    if len(clientes) > 0:
                        funciones.eliminar_cliente()
                    else:
                        print("No hay cliente registrados")
                except:
                    print("No se pudo ejecutar la consulta")
            elif opc == 5:
                run_custom_query(conectar)
            elif opc == 6:
                print("saliendo ......")
                opciones = False
        else:
            print(f"El numero : {opc} no es valido, escriba del 1 al 6")
            conectar.desconectar()


menu_opciones()
