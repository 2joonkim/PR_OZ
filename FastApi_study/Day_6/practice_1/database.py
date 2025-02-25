from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timezone

# 데이터베이스 연결 설정
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 클래스 생성
Base = declarative_base()

# 파일 업로드 모델 정의
class FileUpload(Base):
    __tablename__ = "file_upload"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    upload_time = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    processed_time = Column(DateTime, nullable=True)
    status = Column(String, nullable=True)

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

# 데이터베이스 세션 관리를 위한 의존성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()