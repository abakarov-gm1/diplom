from .base import Base
from sqlalchemy import Column, Integer, String, Boolean, BigInteger
from sqlalchemy.orm import relationship


# предмет по егэ
class Exam(Base):
    __tablename__ = 'exam'

    id = Column(Integer, primary_key=True)
    subject = Column(String)  # предмет
    score = Column(Integer)  # Балл за предмет

    # Связь с таблицей student_exam
    students = relationship(
        'Student',
        secondary="student_exam",
        back_populates='exams'
    )

