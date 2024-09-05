from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for SQLAlchemy ORM models.

    This class serves as the base class for all SQLAlchemy ORM models in the application.

    Attributes:
    - This class does not have any attributes or methods itself but provides a
    common base for other SQLAlchemy models to inherit from.

    Usage:
    To create a model class that uses this base, you would inherit from `Base`:

    ```python
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.orm import relationship

    class ExampleModel(Base):
        __tablename__ = 'example_model'

        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
    ```

    This setup ensures that SQLAlchemy can automatically handle the creation and
    management of tables in the database based on the model definitions.

    Note:
    This class is part of the SQLAlchemy ORM setup and is intended to be used as
    a base class for other ORM model classes.
    """

    pass
