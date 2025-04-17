import logging
from config.database import engine, Base

# Basic logging setup
logging.basicConfig(level=logging.INFO)

def create_tables():
    logging.info("Creating tables...")

    Base.metadata.create_all(bind=engine)

    logging.info("Tables Created Successfully.")
