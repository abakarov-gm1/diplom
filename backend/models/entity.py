from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, TEXT
from sqlalchemy.orm import relationship

from .base import Base


class Entity(Base):
    __tablename__ = 'entity'

    id = Column(Integer, primary_key=True)
    entity = Column(String, nullable=True)
    ogrn = Column(String, nullable=True)
    kpp = Column(String, nullable=True)

    actions = relationship("Actions", back_populates="entity")

