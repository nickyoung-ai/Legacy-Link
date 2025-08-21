from models import Base
from database import engine
# Create the tables in the database
Base.metadata.create_all(bind=engine)
