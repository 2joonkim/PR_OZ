from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./task_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 사용자 데이터베이스
users_db = {}
"""
users_db 구조:
{
    "username": {
        "username": str,
        "email": str,
        "hashed_password": str
    }
}
"""

# 태스크 데이터베이스
tasks_db = {}
task_counter = 0
"""
tasks_db 구조:
{
    task_id: {
        "id": int,
        "title": str,
        "description": str | None,
        "completed": bool,
        "due_date": datetime | None,
        "created_at": datetime,
        "owner": str
    }
}
"""

# 데이터베이스 조작 함수들
def get_user(username: str):
    return users_db.get(username)

def create_user(username: str, email: str, hashed_password: str):
    users_db[username] = {
        "username": username,
        "email": email,
        "hashed_password": hashed_password
    }
    return users_db[username]

def create_task(title: str, description: str, owner: str, due_date: datetime = None):
    global task_counter
    task_counter += 1
    
    new_task = {
        "id": task_counter,
        "title": title,
        "description": description,
        "completed": False,
        "due_date": due_date,
        "created_at": datetime.utcnow(),
        "owner": owner
    }
    tasks_db[task_counter] = new_task
    return new_task

def get_task(task_id: int):
    return tasks_db.get(task_id)

def get_user_tasks(username: str):
    return [task for task in tasks_db.values() if task["owner"] == username]

def update_task(task_id: int, title: str, description: str, due_date: datetime = None):
    if task_id in tasks_db:
        tasks_db[task_id].update({
            "title": title,
            "description": description,
            "due_date": due_date
        })
        return tasks_db[task_id]
    return None

def delete_task(task_id: int):
    if task_id in tasks_db:
        del tasks_db[task_id]
        return True
    return False

def complete_task(task_id: int):
    if task_id in tasks_db:
        tasks_db[task_id]["completed"] = True
        return tasks_db[task_id]
    return None
