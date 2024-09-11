from dotenv import load_dotenv
import os  # for os.environ is used to access the environment variables

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Desactiva las notificaciones de modificaciones

