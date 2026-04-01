from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    All your database models will inherit from this class.
    It acts as a 'catalog' of your tables for SQLAlchemy and Alembic.
    """

    pass
