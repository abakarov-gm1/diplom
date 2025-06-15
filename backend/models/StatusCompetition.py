from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, UUID, ForeignKey, BigInteger
from .base import Base


class StatusCompetition(Base):
    __tablename__ = 'status_competition'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    actual = Column(Boolean, default=False)


