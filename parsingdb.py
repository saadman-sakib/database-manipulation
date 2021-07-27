from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, engine, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    image_file = Column(String, nullable=False, default='default.jpg')
    password = Column(String, nullable=False)
    posts = relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(Base):
    __tablename__ = "post"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    date_posted = Column(DateTime, nullable=False, default=datetime.utcnow)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


engine = create_engine('sqlite:///site.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# querying data
users = session.query(User).all()
posts = session.query(Post).all()
print(
'''
###########################################
################  USERS  ##################
###########################################
'''
)
for user in users:
    print(f"id: {user.id}   name: {user.username}")

print(
'''
###########################################
################  POSTS  ##################
###########################################
'''
)
for post in posts:
    print(f"id: {post.id}   title: {post.title}")

# session ended #
session.close()
