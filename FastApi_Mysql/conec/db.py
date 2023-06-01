from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:@localhost:3306/users")

# Crear el objeto metadata
meta = MetaData()

# Crear la conexión a la base de datos
conn = engine.connect()


                                











