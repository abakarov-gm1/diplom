# from sqlalchemy.orm import relationship
# from .base import Base
# from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
#
#
# # направление подготовки
# class Direction(Base):
#     __tablename__ = 'direction'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     code = Column(Integer)
#
#     # связь с заявкой
#     statement = relationship("Statement", back_populates="direction")
#
#
# models/direction.py
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
