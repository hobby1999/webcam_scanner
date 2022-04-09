from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlitedb/scannerdb.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def getdb():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()