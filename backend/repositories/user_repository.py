from models.users import User
from config import get_session


class UserRepository:
    def __init__(self):
        pass

    def register_user(self, username, password):
        with get_session() as session:
            new_user = User(username=username, password=password)
            session.add(new_user)
            session.commit()

    def login_user(self, phone, password):
        with get_session() as session:
            user = session.query(User).filter(User.phone == phone).first()
            return user


