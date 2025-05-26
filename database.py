from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import seessionmaker 

#SQLite database URL
SQLALCHEMY_DATABASE_URL="sqlite:"