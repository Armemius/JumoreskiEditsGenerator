import os
import sqlite3
import spdlog as spd
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_PATH = "data/database.sqlite"
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
logger = spd.ConsoleLogger("storage")

if not os.path.exists(DATABASE_PATH):
    conn = sqlite3.connect(DATABASE_PATH)
    conn.close()
    logger.info(f"Database created at: {DATABASE_PATH}")
else:
    logger.info(f"Database already exists at: {DATABASE_PATH}")

engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
