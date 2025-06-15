from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, UUID
from .base import Base


class Competition(Base):
    __tablename__ = 'competitions'

    id = Column(Integer, primary_key=True)  # Уникальный идентификатор записи (Id)
    uid = Column(UUID(as_uuid=True), unique=True, nullable=True)  # Уникальный идентификатор (Uid)

    ogrn_owner_organization = Column(String(20), nullable=True)  # ОГРН организации-владельца (OgrnOwnerOrganization)
    kpp_owner_organization = Column(String(20), nullable=True)  # КПП организации-владельца (KppOwnerOrganization)

    id_campaign = Column(Integer, nullable=True)  # Идентификатор приёмной кампании (IdCampaign)
    id_direction = Column(Integer, nullable=True)  # Идентификатор направления подготовки (IdDirection)

    comment = Column(String, nullable=True)  # Комментарий, например "КИЗЛЯР Таможенное дело (очно, платно)" (Comment)

    id_education_level = Column(Integer, nullable=True)  # Уровень образования (бакалавриат, магистратура и т.п.) (IdEducationLevel)
    id_education_form = Column(Integer, nullable=True)  # Форма обучения (очная, заочная и т.д.) (IdEducationForm)
    id_place_type = Column(Integer, nullable=True)  # Тип места (бюджет/контракт и т.п.) (IdPlaceType)

    number_places = Column(Integer, nullable=True)  # Количество мест на направлении (NumberPlaces)
    id_stage_admission = Column(Integer, nullable=True)  # Этап приёма (например, первый, дополнительный и т.д.) (IdStageAdmission)

    only_for_foreigners = Column(Boolean, default=False)  # Только для иностранных граждан (OnlyForForeigners)
    only_citizens_rf = Column(Boolean, default=False)  # Только для граждан РФ (OnlyCitizensRF)
    second_education_arts = Column(Boolean, default=False)  # Для лиц, получающих второе образование в сфере искусств (SecondEducationArts)
    preview_tours = Column(Boolean, default=False)  # Наличие предварительных туров (например, собеседование, прослушивание) (PreviewTours)
    attaching_portfolio = Column(Boolean, default=False)  # Требуется прикрепление портфолио (AttachingPortfolio)
    medical_examination = Column(Boolean, default=False)  # Требуется медосмотр (MedicalExamination)

    id_educational_program = Column(Integer, nullable=True)  # Идентификатор образовательной программы (из EducationalProgramList → IdEducationalProgram)

    only_for_vo = Column(Boolean, default=False)  # Только для лиц с ВО (высшим образованием) (OnlyForVo)
    only_for_spo = Column(Boolean, default=False)  # Только для лиц с СПО (средним профессиональным образованием) (OnlyForSpo)

    cost_of_study = Column(Integer, nullable=False, default=0)  # Стоимость обучения (CostOfStudy)
    approved_foiv = Column(Boolean, default=False)  # Программа утверждена ФОИВ (федеральным органом) (ApprovedFoiv)
