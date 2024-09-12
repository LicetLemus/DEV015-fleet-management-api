import pytest
from app import create_app, db
from app.config import TestingConfig
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="module")
def test_client():
    app = create_app(TestingConfig)
    
    # Configurar la base de datos de pruebas
    with app.app_context():
        # db.drop_all()
        # Crear tablas nuevas
        db.create_all()

    with app.test_client() as testing_client:
        yield testing_client

    with app.app_context():
        # Limpiar la base de datos después de las pruebas
        db.drop_all()
        db.session.remove()
