from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, UUID, ForeignKey, BigInteger, Date
from .base import Base


class ApplicationList(Base):
    __tablename__ = 'application'

    id = Column(Integer, primary_key=True)
    id_epgu = Column(Integer, nullable=True)
    id_entrant = Column(Integer, nullable=True)
    registration_date = Column(Date, nullable=True)
    actual = Column(Boolean, default=False)
    id_education_level_group = Column(Integer)

