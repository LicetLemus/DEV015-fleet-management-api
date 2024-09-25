from dotenv import load_dotenv
import os  # for os.environ is used to access the environment variables

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Desactiva las notificaciones de modificaciones
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL")
    SECRET_KEY = os.getenv("TEST_SECRET_KEY")
    # ACCESS_TOKEN = os.getenv("TEST_ACCESS_TOKEN")