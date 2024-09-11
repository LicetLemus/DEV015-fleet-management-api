from flask import Flask
from app.database.db_sql import db
from app.routes.main import bp_main
from app.routes.taxi_routes import bp_taxis
from app.routes.trajectory_routes import bp_location
from app.routes.trajectory_latest_routes import bp_latest
from app.routes.user_routes import bp_user

from app.models.users import Users


def create_app():
    """
    Creates and configures an instance of the Flask application.
    This function initializes the Flask application, loads configuration settings, and registers blueprints to organize the routes of the application.

    Returns:
        Flask: An instance of the Flask application with configurations and routes set up.
    """

    app = Flask(__name__)  # create of  instance of the Flask class
    # configuration
    app.config.from_object(
        "app.config.Config"
    )  # load the configuration from the config.py file

    # Inicializar sqlalchemy con la aplicaion
    db.init_app(app)

    # Import and register the blueprint: Blueprint is a way to organize the routes of the application.
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_taxis)
    app.register_blueprint(bp_location)
    app.register_blueprint(bp_latest)
    app.register_blueprint(bp_user)

    try:
        with app.app_context():
            db.create_all()
    except Exception as e:
        print(f"Error al crear las tablas: {e}")
    return app
