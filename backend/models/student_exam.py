from sqlalchemy.orm import relationship
from .base import Base
from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey


class StudentExam(Base):
    __tablename__ = 'student_exam'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    exam_id = Column(Integer, ForeignKey('exam.id'))

    # Связи
    student = relationship('Student', back_populates='exams')
    exam = relationship('Exam', back_populates='students')

