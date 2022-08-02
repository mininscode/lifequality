from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings as _settings


DB_NAME = _settings.DATABASE_NAME
DB_USER = _settings.DATABASE_USERNAME
DB_PASS = _settings.DATABASE_PASSWORD
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@localhost:5432/{DB_NAME}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

