from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

import os

load_dotenv()

MYSQL_USER=os.getenv("MYSQL_USER")
MYSQL_DB=os.getenv("MYSQL_DB")
MYSQL_HOST=os.getenv("MYSQL_HOST")
MYSQL_PASSWORD=os.getenv("MYSQL_PASSWORD")
MYSQL_PORT=os.getenv("MYSQL_PORT")


database_url=f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

engine=create_engine(database_url)
sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)


Base=declarative_base()

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()