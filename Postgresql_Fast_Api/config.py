from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# connection en postgres local
#url = "postgresql://postgres:bosonit@localhost:5432/biblioteca"

#url = "postgresql://root:admin@192.168.10.47:5432/biblioteca"

# connection en mariadb portainer
url = "mysql+pymysql://root:admin123@localhost:3307/biblioteca"

#url = 'mysql+pymysql://root:@192.168.131.41:90/biblioteca'

engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


