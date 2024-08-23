# configure the Flask application and of extensiones with sqlalchemy.
# Compare this snippet from app/__init__.py: 

from flask import Flask
from sqlalchemy import create_engine
from app.config import database_url
from .routes.taxis import register_routes

# create of instance of the Flask class

def create_app():
    app = Flask(__name__) # create of instance of the Flask class
    
    engine = create_engine(database_url) # is the connection to the database
    app.engine = engine
    
    # Import and register the blueprint: Blueprint is a way to organize the routes of the application.
    register_routes(app, engine)
    
    return app