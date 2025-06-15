from config import get_session
from models import CompetitionGroup
from sqlalchemy.orm import joinedload


def get_competition_group_id_array():
    with get_session() as session:
        id_array = [item.competition_id for item in session.query(CompetitionGroup.competition_id).all()]
        return id_array


def add_group_competition(
        competition_id,
        application_id,
        direction_id,
        status_id,
        is_ovo,
        education_form_id,
        place_type_id
):
    with get_session() as session:
        cg = CompetitionGroup(
            competition_id=competition_id,
            application_id=application_id,
            direction_id=direction_id,
            status_id=status_id,
            is_ovo=is_ovo,
            education_form_id=education_form_id,
            place_type_id=place_type_id
        )
        session.add(cg)
        session.commit()








