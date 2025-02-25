from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite 메모리 데이터베이스 연결
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

session = SessionLocal()
new_user = User(name="John Doe")
session.add(new_user)
session.commit()

users = session.query(User).all()
for user in users:
    print(user.name)

