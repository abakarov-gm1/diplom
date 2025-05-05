from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from .base import Base


class Statement(Base):
    __tablename__ = 'statement'

    id = Column(Integer, primary_key=True)
    form_education = Column(String)  # (форма очно заочно)
    date_created = Column(DateTime)
    status = Column(String)  # Отозван/Зачислен/на проверке
    student_id = Column(Integer, ForeignKey('student.id'))

    # связи
    directions = relationship(
        "Direction",
        secondary="direction_statement",
        back_populates="statements"
    )
    student = relationship('Student', back_populates='statements')

