from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, TEXT
from sqlalchemy.orm import relationship

from .base import Base


class Entrant(Base):
    __tablename__ = 'entrants'

    id = Column(Integer, primary_key=True, autoincrement=False)  # соответствует "Id"
    unique_code_profile = Column(String, nullable=False)        # соответствует "UniqueCodeProfile"
    snils = Column(String, nullable=True)                       # соответствует "Snils"
    surname = Column(String, nullable=False)                    # соответствует "Surname"
    name = Column(String, nullable=False)                       # соответствует "Name"
    patronymic = Column(String, nullable=True)                  # соответствует "Patronymic"