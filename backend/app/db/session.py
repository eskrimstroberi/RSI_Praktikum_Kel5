from sqlmodel import create_engine, Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    db = SessionLocal()
    try:
        with Session(engine) as session:
            yield session
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()
