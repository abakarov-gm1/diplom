from models.DerictionCls import DirectionCls
from config import get_session


def get_one_direction(self, direction_id):
    with get_session() as session:
        return (
            session.query(DirectionCls)
            .filter(DirectionCls.id == direction_id)
            .first()
        )


# def get_add_directions(name, code, actual, section_id, education_level_id, parent_id):
#     with get_session() as session:
#         directions = DirectionCls(
#             name=name, code=code,
#             actual=actual,
#             section_id=section_id,
#             education_level_id=education_level_id,
#             parent_id=parent_id
#         )
#         session.add(directions)
#         session.commit()
#         return True


def get_add_directions_bulk(directions_data: list[dict]):

    with get_session() as session:
        directions = [
            DirectionCls(
                Id_Direction=item.get("Id"),
                name=item.get("Name") if item.get("Name") else "",
                code=item.get("Code") if item.get("Code") else "",
                actual=True if item.get("Actual") == "true" else False if item.get("Actual") else None,
                section_id=item.get("Section") if item.get("Section") else None,
                education_level_id=item.get("IdEducationLevel") if item.get("IdEducationLevel") else None,
                parent_id=item.get("IdParent") if item.get("IdParent") else None
            )
            for item in directions_data
        ]
        session.add_all(directions)
        session.commit()
        return True

