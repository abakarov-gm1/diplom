# from sqlalchemy.orm import relationship
# from .base import Base
# from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
#
#
# class Statement(Base):
#
#     __tablename__ = 'statement'
#
#     id = Column(Integer, primary_key=True)
#     form_education = Column(String)  # (форма очно заочно)
#     date_created = Column(DateTime)
#
#     status = Column(Integer)  # Отозван/Зачислен
#     form_of_education = Column(Integer)  # Форма обучения (очно/заочно)
#     data = Column(DateTime)  # Дата (странный тип, лучше DATE или DATETIME)
#     student_id = Column(Integer, ForeignKey('student.id'))
#
#     #
#     direction = relationship("Direction", back_populates="statement")
#
#     # связь с студентом
#     student = relationship('Student', back_populates='statements')
#
#



# models/statement.py
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from .base import Base


class Statement(Base):
    __tablename__ = 'statement'

    id = Column(Integer, primary_key=True)
    form_education = Column(String)
    date_created = Column(DateTime)
    status = Column(Integer)
    form_of_education = Column(Integer)
    data = Column(DateTime)
    student_id = Column(Integer, ForeignKey('student.id'))

    # связи
    directions = relationship(
        "Direction",
        secondary="direction_statement",
        back_populates="statements"
    )
    student = relationship('Student', back_populates='statements')



# исправить таблицы
# исправить поля, разобрать relationship
# сделать фронтенд кликабельным
