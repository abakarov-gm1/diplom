import redis
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# UPLOAD_DIR = os.getenv('UPLOAD_DIR')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

redis_client = redis.Redis(host="redis", port=6379, decode_responses=True)


engine = create_engine(
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@database/{POSTGRES_DB}", echo=True)


Session = sessionmaker(bind=engine)


def get_session():
    return Session()
