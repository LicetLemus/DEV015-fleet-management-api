import pytest
from app import create_app, db
from app.config import TestingConfig
from dotenv import load_dotenv


load_dotenv()


@pytest.fixture(scope="module")
def test_client():
    # Create an instance of the app with the testing configuration
    app = create_app(TestingConfig)

    # start the app context for initial setup
    with app.app_context():
        # db.drop_all()
        # create the tables in the database for testing
        db.create_all()

    # create a test client to simulate HTTP requests
    with app.test_client() as testing_client:
        # yield the test client for use in tests
        yield testing_client

    # Reinitialize the app context to clean up the database 
    with app.app_context():
        # drop all tables after testes are finished
        db.drop_all()
        # Close any active database sessions
        db.session.remove()
