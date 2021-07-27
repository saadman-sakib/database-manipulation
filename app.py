from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, unique=True)

engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
# session starter #

# creating and adding data in session
user = User()
user.id = 0
user.name = "Saadman"
session.add(user)
session.commit()


# querying data
users = session.query(User).filter(User.name == "Saadman").all()
for user in users:
    print(f"id: {user.id}   name: {user.name}")

# session ended #
session.close()
