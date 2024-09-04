# configure the Flask application and of extensiones with sqlalchemy.
# Compare this snippet from app/__init__.py: 

from flask import Flask
from app.routes.main import bp_main 
from app.routes.taxis_routes import bp_taxis
from app.routes.trajectories_routes import bp_location
from app.routes.trajectory_lastest import bp_latest

# create of instance of the Flask class

def create_app():
    """
    Creates and configures an instance of the Flask application.
    This function initializes the Flask application, loads configuration settings, and registers blueprints to organize the routes of the application.

    Returns:
        Flask: An instance of the Flask application with configurations and routes set up.
    """

    app = Flask(__name__) # create of  instance of the Flask class
    # configuration
    app.config.from_object('app.config.Config') # load the configuration from the config.py file
    
    # Import and register the blueprint: Blueprint is a way to organize the routes of the application.
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_taxis)
    app.register_blueprint(bp_location)
    app.register_blueprint(bp_latest)
    
    return app