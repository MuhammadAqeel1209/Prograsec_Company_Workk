import logging
from config.database import engine, Base
from models.students import Student

# Basic logging setup
logging.basicConfig(level=logging.INFO)

Student.__table__.drop(engine)
def create_tables():
    logging.info("Creating tables...")
    Base.metadata.create_all(bind=engine)

    logging.info("Tables Created Successfully.")
