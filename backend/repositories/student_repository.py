from models.student import Student
from config import get_session


class StudentRepository:

    def __init__(self):
        pass

    def get_students(self):
        with get_session() as session:
            students = session.query(Student).all()
            return students






