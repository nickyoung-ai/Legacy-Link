from sqlalchemy import Column ,Integer,String, Text
from database import Base

from database import Base

class User(Base):
    __tablename__= "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email=Column(String, unique=True, index=True)
    hashed=password=Column(String)

    bio= Column (Text, nullable=True)
    profile_picture_url = Column(String, nullable=True) 
    location= Column(String, nullable=True)
    links = Column(String, nullable=True)
     # Assuming bio is a text field, adjust as necessary