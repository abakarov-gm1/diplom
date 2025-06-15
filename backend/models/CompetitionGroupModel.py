from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, UUID, ForeignKey, BigInteger
from .base import Base


class CompetitionGroup(Base):
    __tablename__ = 'competition_group'

    id = Column(Integer, primary_key=True)
    # competition_id = Column(BigInteger, nullable=True)  # группа конкурса
    competition_id = Column(BigInteger, ForeignKey('competitions.id'))
    application_id = Column(BigInteger, nullable=True)  # id заявки
    direction_id = Column(BigInteger, nullable=True)  # направление обучения
    status_id = Column(Integer, nullable=True)  # зачислен не зачислен все дела
    is_ovo = Column(Boolean, default=False)  # От ООВО (вуз вручную) или нет (false = через ЕПГУ)
    education_form_id = Column(Integer, nullable=True)  # Форма обучения (1 — очная и т.п.)	Из справочника EducationFormCls
    place_type_id = Column(Integer, nullable=True)  # Тип места (бюджет, контракт и т.д.)	Из справочника PlaceTypeCls

    competition = relationship("Competition", back_populates="groups")
