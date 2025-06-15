from config import get_session
from models.EducationLevelCls import EducationLevelCls


def get_one_education(education_id):
    with get_session() as session:
        return (
            session.query(EducationLevelCls)
            .filter(EducationLevelCls.id == education_id)
            .first()
        )


def get_add_education_level_bulk(education_data: list[dict]):

    with get_session() as session:
        directions = [
            EducationLevelCls(
                id_level_cls=item.get("Id"),
                name=item.get("Name") if item.get("Name") else "",
                actual=True if item.get("Actual") == "true" else False if item.get("Actual") else None,
                education_level_group_id=item.get("IdEducationLevelGroup") if item.get("IdEducationLevelGroup") else None,
            )
            for item in education_data
        ]
        session.add_all(directions)
        session.commit()
        return True

