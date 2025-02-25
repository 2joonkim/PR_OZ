from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer

# JWT 설정
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 비밀번호 해싱 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 가짜 사용자 데이터베이스 (role 추가됨)
fake_users_db = {
    "admin": {"username": "admin", "password": pwd_context.hash("adminpass"), "role": "admin"},
    "testuser": {"username": "testuser", "password": pwd_context.hash("testpass"), "role": "user"}
}

# FastAPI 앱 초기화
app = FastAPI()

# OAuth2 Bearer 토큰 설정
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Pydantic 모델
class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserUpdate(BaseModel):
    username: str

# 비밀번호 해싱 함수
def hash_password(password: str):
    return pwd_context.hash(password)

# 비밀번호 검증 함수
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# JWT 토큰 생성 함수
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 사용자 검증 함수
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        exp = payload.get("exp")

        if username is None or exp is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        # 토큰 만료 체크
        if datetime.utcnow() > datetime.utcfromtimestamp(exp):
            raise HTTPException(status_code=401, detail="Token has expired")

        user = fake_users_db.get(username)
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")

        return user  # 사용자 정보 반환

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Register API
@app.post("/register")
def register(user: UserRegister):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = hash_password(user.password)
    fake_users_db[user.username] = {"username": user.username, "password": hashed_password, "role": "user"}
    return {"message": "User registered successfully"}

# Login API
@app.post("/login", response_model=Token)
def login(user: UserLogin):
    db_user = fake_users_db.get(user.username)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    access_token = create_access_token(data={"sub": user.username, "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    return {"access_token": access_token, "token_type": "bearer"}

# GET Profile API
@app.get("/profile")
def get_profile(current_user: dict = Depends(get_current_user)):
    return {"username": current_user["username"]}

######################################################################
# ✅ 쉬움: 현재 로그인한 사용자의 토큰 만료 시간 가져오기
######################################################################
@app.get("/token-expiry")
def get_token_expiry(current_user: dict = Depends(get_current_user), token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    exp_timestamp = payload.get("exp")

    if exp_timestamp is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    exp_time = datetime.utcfromtimestamp(exp_timestamp).isoformat() + "Z"
    
    return {"username": current_user["username"], "expires_at": exp_time}

######################################################################
# ✅ 보통: 관리자만 접근 가능한 `/admin` API
######################################################################
@app.get("/admin")
def admin_access(current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Access denied. Admins only.")
    
    return {"message": "Welcome, admin!"}

######################################################################
# ✅ 어려움: 사용자 프로필 수정 API (`PUT /profile`)
######################################################################
@app.put("/profile")
def update_profile(user_update: UserUpdate, current_user: dict = Depends(get_current_user)):
    username = current_user["username"]

    # 기존 유저 정보 업데이트 (단, 비밀번호는 변경 불가능)
    fake_users_db[username]["username"] = user_update.username

    return {
        "message": "Profile updated successfully",
        "updated_user": {"username": user_update.username}
    }