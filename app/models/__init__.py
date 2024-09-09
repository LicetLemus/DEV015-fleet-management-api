from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for SQLAlchemy ORM models.

    Provides a common base for all SQLAlchemy models. Inherit from this class to define ORM models.

    Example:
        class ExampleModel(Base):
            __tablename__ = 'example_model'
            id = Column(Integer, primary_key=True)
            name = Column(String)
    """

    pass
