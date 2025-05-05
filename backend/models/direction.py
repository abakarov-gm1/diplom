# направление подготовки
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from .base import Base


class Direction(Base):
    __tablename__ = 'direction'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(Integer)

    # связи
    statements = relationship(
        "Statement",
        secondary="direction_statement",
        back_populates="directions"
    )
