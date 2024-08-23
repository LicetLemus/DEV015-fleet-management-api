# conected to the database and execute the sql query

from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def get_connection():
    
    try:
        load_dotenv()
        database_url = os.getenv("DATABASE_URL")
        engine = create_engine(database_url) # create_engine: is used to create a new database connection
        connection = engine.connect() # engine.connect: is used to connect to the database
        print("Connected to database")
        return connection # return the connection
    
    except Exception as e:
        print("Error al conectar con la base de datos ", e)
    