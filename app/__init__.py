from flask import Flask
from app.database.db_sql import db
from app.config import Config
from flask_jwt_extended import JWTManager

from app.routes.main import bp_main
from app.routes.taxi_routes import bp_taxis
from app.routes.trajectory_routes import bp_location
from app.routes.trajectory_latest_routes import bp_latest
from app.routes.user_routes import bp_user
from app.routes.auth import bp_auth

from app.models.users import Users


def create_app(config_class=Config):
    """
    Creates and configures an instance of the Flask application.
    This function initializes the Flask application, loads configuration settings, and registers blueprints to organize the routes of the application.

    Returns:
        Flask: An instance of the Flask application with configurations and routes set up.
    """

    app = Flask(__name__)  # create of  instance of the Flask class
    # configuration
    app.config.from_object(config_class)

    # Initialize sqlalchemy with the application
    db.init_app(app)
    jwt = JWTManager(app)

    # Import and register the blueprint: Blueprint is a way to organize the routes of the application.
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_taxis)
    app.register_blueprint(bp_location)
    app.register_blueprint(bp_latest)
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_auth)

    # jwt error handling
    
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return {"error": "The token has expired."}, 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return {"error": "The token is invalid or expired."}, 401

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return {"error": "You are not authorized to access this resource."}, 401

    # create tables for the database
    try:
        with app.app_context():
            db.create_all()
    except Exception as e:
        print(f"Error al crear las tablas: {e}")

    return app
