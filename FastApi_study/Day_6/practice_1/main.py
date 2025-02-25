from fastapi import FastAPI, File, UploadFile, BackgroundTasks, Depends
from sqlalchemy.orm import Session
from database import get_db, FileUpload
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # 저장 폴더 생성

# 오류 없는 파일 업로드
def save_file(filename: str, content: bytes):
    with open(os.path.join(UPLOAD_DIR, filename), "wb") as f:
        f.write(content)
    print(f"파일 저장 완료: {filename}")

# ValueError: I/O operation on closed file. 발생
# def save_file(file: UploadFile):
#     with open(f"uploads/{file.filename}", "wb") as f:
#         f.write(file.file.read())
#     print(f"파일 저장 완료: {file.filename}")

def log_file_upload(filename: str, db: Session):
    new_record = FileUpload(filename=filename, status="Saved")
    db.add(new_record)
    db.commit()
    print(f"로그 저장 완료: {filename}")

@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks(), db: Session = Depends(get_db)):
    file_content = await file.read()  # 파일을 미리 읽어서 백그라운드 작업으로 전달
    background_tasks.add_task(save_file, file.filename, file_content)
    background_tasks.add_task(log_file_upload, file.filename, db)
    return {"message": "파일 업로드 중..."}