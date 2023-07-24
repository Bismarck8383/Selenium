import os
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


class ConexionDB:
    # Datos de connexion:
    config = {
        'user': 'root',
        'password': 'admin123',
        'host': '192.168.10.47',
        'port': '3307',
        'database': 'crud'
    }
    CONN = f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"

    @classmethod
    def get_engine(cls):
        return create_engine(cls.CONN)


# Definición de Base usando automap
Base = automap_base()

# Motor de DB
engine = ConexionDB.get_engine()

# Reflejando las tablas
Base.prepare(engine, reflect=True)

# Accediendo a la tabla 'cliente'
Cliente = Base.classes.cliente

# Creando una sesión
session = Session(engine)

# Ahora puedes usar session para interactuar con la base de datos,
# y la clase Cliente para interactuar con la tabla 'cliente'.

# Ejemplo: Obtener todos los clientes
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(cliente.id)  # Asume que 'id' es una columna en la tabla 'cliente'

session.close()
