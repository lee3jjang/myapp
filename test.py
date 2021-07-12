# %%
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# %%
engine = create_engine('sqlite:///test.db')
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# %%
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'TestUser'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
# %%
Base.metadata.create_all(engine)
# %%
db = SessionLocal()
# %%
# db.rollback()
# db_user = User(email='asdf', password='32323')
# db.add(db_user)
# db.commit()
