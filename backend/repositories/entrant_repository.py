from config import get_session
from models.EntrantList import Entrant


def get_all_entrant():
    with get_session() as session:
        return session.query(Entrant).all()


def add_all_entrant(data):
    with get_session() as session:
        e = [
            Entrant(
                id=item.get("Id"),
                unique_code_profile=item.get("UniqueCodeProfile", ''),
                snils=True if item.get("Snils", '') == 'true' else False,
                surname=item.get("Surname", ''),
                name=item.get("Name", ''),
                patronymic=item.get("Patronymic", ''),
            )
            for item in data
        ]
        session.add_all(e)
        session.commit()
