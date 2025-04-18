import logging
from config.database import engine, Base
# from models.students import Student

# Basic logging setup
logging.basicConfig(level=logging.INFO)

def create_tables():
    # Student.__table__.drop(bind=engine)
    logging.info("Creating tables...")
    Base.metadata.create_all(bind=engine)

    logging.info("Tables Created Successfully.")
