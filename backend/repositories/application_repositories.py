from models.StatusCompetition import StatusCompetition
from config import get_session
from models.ApplicationList import ApplicationList
from datetime import datetime, date


def get_all_applications():
    with get_session() as session:
        return session.query(ApplicationList).all()


def add_applications_from_super_service(applications):
    with get_session() as session:
        new_object_applications = [
            ApplicationList(
                id=item.get("Id", None),
                id_entrant=int(item.get("IdEntrant", None)),
                registration_date=datetime.fromisoformat(item["RegistrationDate"]).date()
                if item.get("RegistrationDate") else None,
                actual=True if item.get("Actual", False) == 'true' else False,
                id_education_level_group=int(item.get("IdEducationLevelGroup", None))
            ) for item in applications]

        session.add_all(new_object_applications)
        session.commit()

