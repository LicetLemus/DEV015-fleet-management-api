# conected to the database and execute the sql query

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from dotenv import load_dotenv
import os

# load of variable of environment
load_dotenv()
database_url = os.getenv("DATABASE_URL")

# create of a new database connection - motor 
engine = create_engine(database_url) 

# class of SQLAlchemy that create a new instance of session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    try:
        return SessionLocal() # return of instance session
    
    except Exception as e:
        print("Error al conectar con la base de datos ", e)
        return None
    