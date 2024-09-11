"""
This module initializes and configures Flask extensions used in the application.
Currently, it includes the SQLAlchemy extension for ORM (Object-Relational Mapping).

- `db`: An instance of SQLAlchemy used for managing database connections and operations.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
