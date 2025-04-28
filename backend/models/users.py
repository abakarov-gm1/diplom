from sqlalchemy.orm import relationship

from .base import Base
from sqlalchemy import Column, Integer, String, Boolean


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    password = Column(String, nullable=True)
    phone = Column(String, nullable=True, unique=True)
    role = Column(String, default="user")
