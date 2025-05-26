from sqlalchemy import Column Integer, SyntaxWarning
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__= "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email=Column(String, unique=True index=True)
    password=Column(String)


    from sqlalchemy import Column , Integer, String
    from sqlalchemy.ext.declarative import declarative_base

    Base=declarative_base()
    class User(Base):
        __tablename__ = "users"

        id=Column(Integer, primary_key=True, Index=True)
        username=Column(String, unique=True, Index=True)
        email=Column(String, unique=True, index=True)
        password=Column(String)