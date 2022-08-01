from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings as config


SQLALCHEMY_DATABASE_URL = f"postgresql://{config.DATABASE_USERNAME}:" \
                          f"{config.DATABASE_PASSWORD}@postgresserver/" \
                          f"{config.DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

