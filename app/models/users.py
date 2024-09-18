from app.database.db_sql import db
from sqlalchemy import Column, Integer, String


class Users(db.Model):
    """
    SQLAlchemy ORM model for the 'users' table.

    Attributes:
    - id (int): Unique identifier for the user.
    - name (str): Name of the user.
    - email (str): User's email address (unique).
    - password (str): User's hashed password.

    Example:
        new_user = Users(
            id=1,
            name='John Doe',
            email='john.doe@example.com',
            password='hashed_password'
        )
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(80), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
