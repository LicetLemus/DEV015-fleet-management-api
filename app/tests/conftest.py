import pytest
from app import create_app, db
from app.config import TestingConfig
from dotenv import load_dotenv
from app.models.taxis import Taxis
from app.models.trajectories import Trajectories

from flask_jwt_extended import create_access_token


load_dotenv()


# token of test
def get_test_token():
    app = create_app(TestingConfig)
    with app.app_context():
        # Create a test token
        return create_access_token(identity='test@gmail.com')


@pytest.fixture(scope="module")
def test_client():
    # Create an instance of the app with the testing configuration
    app = create_app(TestingConfig)

    # start the app context for initial setup
    with app.app_context():
        db.drop_all()
        # create the tables in the database for testing
        db.create_all()

        db.session.add(Taxis(id=1, plate="CCKF-1601"))
        db.session.add(Taxis(id=2, plate="SDFE-6754"))

        db.session.add(
            Trajectories(
                taxi_id=1,
                date="Sat Feb 02 2008 12:37:40",
                latitude=117.45367,
                longitude=118.72647,
            )
        )
        db.session.add(
            Trajectories(
                taxi_id=1,
                date="Sat Feb 07 2008 12:37:40",
                latitude=113.45367,
                longitude=117.72647,
            )
        )
        db.session.add(
            Trajectories(
                taxi_id=1,
                date="Sat Feb 08 2008 12:37:40",
                latitude=114.45367,
                longitude=110.72647,
            )
        )

        db.session.commit()

    # Generate a test token
    access_token = get_test_token()

    # create a test client to simulate HTTP requests
    with app.test_client() as testing_client:

        # Set the authorization header with the test token
        testing_client.environ_base["HTTP_AUTHORIZATION"] = f"Bearer {access_token}"

        # yield the test client for use in tests
        yield testing_client

    # Reinitialize the app context to clean up the database
    with app.app_context():
        # drop all tables after testes are finished
        db.drop_all()
        # Close any active database sessions
        db.session.remove()
