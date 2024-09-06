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

# class of SQLAlchemy that create a new instance of session, puente entre la conexion y nuestros modelos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    """
    Create and return a new SQLAlchemy session instance.

    This function establishes a connection to the database using SQLAlchemy's `sessionmaker`.
    It loads the database URL from environment variables and creates a session object bound
    to the engine created with that URL. If an error occurs while creating the session,
    it prints an error message.

    Returns:
    - Session: An instance of SQLAlchemy session if the connection is successful.
    - None: If there is an error while connecting to the database.
    pass
    """

    try:
        return SessionLocal()  # return of instance session

    except Exception as e:
        print("Error al conectar con la base de datos ", e)
        return None
