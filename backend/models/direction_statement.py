# from sqlalchemy.orm import relationship
# from .base import Base
# from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey
#
#
# class DirectionStatement(Base):
#     __tablename__ = 'direction_statement'
#
#     id = Column(Integer, primary_key=True)
#     statement_id = Column(Integer, ForeignKey('statement.id'))
#     direction_id = Column(Integer, ForeignKey('direction.id'))
#
#     # Связи
#     statement = relationship("Statement", back_populates='direction')
#     direction = relationship("Direction", back_populates='statement')
#

# models/direction_statement.py
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey
from .base import Base


class DirectionStatement(Base):
    __tablename__ = 'direction_statement'

    id = Column(Integer, primary_key=True)
    statement_id = Column(Integer, ForeignKey('statement.id'))
    direction_id = Column(Integer, ForeignKey('direction.id'))
