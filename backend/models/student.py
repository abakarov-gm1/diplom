from .base import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship


class Student(Base):

    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    middle_name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    phone = Column(String, nullable=True, unique=True)
    email = Column(String, nullable=True)
    location = Column(String, nullable=False)
    status = Column(String, nullable=False)

    # Связь с экзаменами
    exams = relationship(
        'Exam',
        secondary='student_exam',
        back_populates='students'
    )

    # Связь с заявками
    statements = relationship('Statement', back_populates='student')

