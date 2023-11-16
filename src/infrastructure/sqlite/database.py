from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL


url = URL.create(
    drivername='postgresql+psycopg2',
    username='test-db',
    host='postgres',
    database='test-bulk',
    password='test+4304+',
    port=5432
)

engine = create_engine(
    url=url
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


Base = declarative_base()


def create_tables():
    Base.metadata.create_all(bind=engine)
