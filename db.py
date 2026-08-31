import certifi
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL= "mysql+pymysql://4RimPdtA2vwYdC1.root:D8TkUB5h70rNu6fl@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test"

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

