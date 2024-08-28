# configure the Flask application and of extensiones with sqlalchemy.
# Compare this snippet from app/__init__.py: 

from flask import Flask
from app.routes.main import bp_main 
from app.routes.taxis_routes import bp_taxis

# create of instance of the Flask class
app = Flask(__name__) # create of  instance of the Flask class


def create_app():
    # configuration
    app.config.from_object('app.config.Config') # load the configuration from the config.py file
    
    # Import and register the blueprint: Blueprint is a way to organize the routes of the application.
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_taxis)
    
    return app