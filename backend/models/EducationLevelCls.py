from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean
from .base import Base


class EducationLevelCls(Base):
    __tablename__ = 'EducationLevelCls'

    id = Column(Integer, primary_key=True)
    id_level_cls = Column(Integer)
    name = Column(String, nullable=True)
    actual = Column(Boolean, nullable=True)
    education_level_group_id = Column(Integer, nullable=True)


