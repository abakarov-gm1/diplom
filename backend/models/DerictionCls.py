from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean
from .base import Base


class DirectionCls(Base):
    __tablename__ = 'Direction_cls'

    id = Column(Integer, primary_key=True)
    Id_Direction = Column(Integer)
    name = Column(String, nullable=True)
    code = Column(String, nullable=True)
    actual = Column(Boolean, nullable=True)
    section_id = Column(Integer, nullable=True)
    education_level_id = Column(Integer, nullable=True)
    parent_id = Column(Integer, nullable=True)


