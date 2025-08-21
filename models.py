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

    # This line sets up a many-to-many relationship between the User and Battle models.
    # 'relationship' is a SQLAlchemy ORM function that links this model (User) to the Battle model.
    # 'secondary="battle_users"' tells SQLAlchemy to use the 'battle_users' association table to manage the many-to-many relationship.
    # 'back_populates="users"' means that the Battle model should have a corresponding 'users' relationship that refers back to User.
    battles = relationship("Battle", secondary="battle_users", back_populates="users")