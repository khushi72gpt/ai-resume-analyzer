import os
import certifi
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl":{
            "ca": certifi.where()
        }
    }
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

