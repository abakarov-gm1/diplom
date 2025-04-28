import random
import string
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
from schemas.auth_model import Login
from repositories.user_repository import get_user_login_service
from conf.redis import redis_connection
from conf import JWT_SECRET_KEY

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_LIFETIME = 15 * 24 * 60 * 60  # 15 days
ACCESS_TOKEN_TIME = 24 * 15  # 15 days


def create_access_token(data: dict, expires_delta: timedelta = timedelta(hours=ACCESS_TOKEN_TIME)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})  # Устанавливаем время истечения токена
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def generate_random_string(length=20):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def create_refresh_token(access_token: str, user_id: int):
    random_part = generate_random_string()
    last_six = access_token[-6:]  # Последние 6 символов access-токена
    refresh_token = random_part + last_six

    redis_key = f"refresh_token:{user_id}"
    redis_connection().set(redis_key, refresh_token, REFRESH_TOKEN_LIFETIME)
    return refresh_token


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def login_case(data: Login):
    user = get_user_login_service(data.phone)
    if not user:
        return {"message": "user is not found"}

    if not verify_password(data.password, user.password):
        return {"message": "password or phone not verify"}

    if not user.is_verified:
        return {"message": "phone is not verified"}

    # если номер телефона отсутствует в редисе, то создаем новый токен и закидываем его в redis
    # вместе с его токеном, а если номер есть то вытаскиваем токен
    # это нагружает систему
    # лучше использовать черный список токенов

    access_token = create_access_token(data={"user_id": user.id})

    # refresh_token = create_refresh_token(access_token, user.id)

    return {"access_token": access_token}

