from models.StatusCompetition import StatusCompetition
from config import get_session


def add_status_competition(competition_all):
    with get_session() as session:
        c_status = [
            StatusCompetition(
                id=item.get("Id"),
                name=item.get("Name") if item.get("Name") else "",
                actual=True if item.get("Actual") == 'true' else False,
            )
            for item in competition_all
        ]
        session.add_all(c_status)
        session.commit()
        return True
