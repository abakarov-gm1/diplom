from models.entity import Entity
from config import get_session
from sqlalchemy.orm import selectinload

class EntityRepository:

    def __init__(self):
        pass

    def get_entity(self, entity_name):
        with get_session() as session:
            return (
                session.query(Entity)
                .options(selectinload(Entity.actions))
                .filter(Entity.entity == entity_name)
                .first()
            )




