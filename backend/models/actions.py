from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, TEXT
from .base import Base
from sqlalchemy.orm import relationship


class Actions(Base):
    __tablename__ = 'actions'

    id = Column(Integer, primary_key=True)
    action = Column(String, nullable=True)
    payload = Column(TEXT, nullable=True)

    entity_id = Column(Integer, ForeignKey('entity.id'))

    entity = relationship("Entity", back_populates="actions")








