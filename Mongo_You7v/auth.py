from datetime import datetime, timedelta
import json
from typing import Optional
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from models import  User
from jose import JWTError, jwt

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
def get_password_hash(password):
    return pwd_context.hash(password)

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="token")

def authenticate_user(username,password):
    try:
        user=json.loads(User.objects.get(username=username).to_json())
        password_check=pwd_context.verify(password,user['password'])
        return password_check
    except User.DoesNotExist:
        return False

def create_access_token(data: dict, expires_delta: Optional[timedelta]  = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

