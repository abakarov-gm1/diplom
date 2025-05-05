from sqlalchemy import Column, Integer, ForeignKey
from .base import Base


class DirectionStatement(Base):
    __tablename__ = 'direction_statement'

    id = Column(Integer, primary_key=True)
    statement_id = Column(Integer, ForeignKey('statement.id'))
    direction_id = Column(Integer, ForeignKey('direction.id'))


