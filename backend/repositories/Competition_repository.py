from config import get_session
from models.CompetitionList import Competition


def get_add_competition_bulk(competition: list[dict]):

    with get_session() as session:
        try:
            c = [
                Competition(
                    id=item.get("Id"),
                    uid=item.get("Uid", None),

                    ogrn_owner_organization=item.get("OgrnOwnerOrganization", None),
                    kpp_owner_organization=item.get("KppOwnerOrganization", None),

                    id_campaign=item.get("IdCampaign", None),
                    id_direction=item.get("IdDirection", None),

                    comment=item.get("Comment", None),

                    id_education_level=item.get("IdEducationLevel", None),
                    id_education_form=item.get("IdEducationForm", None),
                    id_place_type=item.get("IdPlaceType", None),

                    number_places=item.get("NumberPlaces", None),
                    id_stage_admission=item.get("IdStageAdmission", None),

                    only_for_foreigners=True if item.get("OnlyForForeigners", False) == 'true' else False,
                    only_citizens_rf=True if item.get("OnlyCitizensRF", False) == 'true' else False,
                    second_education_arts=True if item.get("SecondEducationArts", False) == 'true' else False,
                    preview_tours=True if item.get("PreviewTours", False) == 'true' else False,
                    attaching_portfolio=True if item.get("AttachingPortfolio", False) == 'true' else False,
                    medical_examination=True if item.get("MedicalExamination", False) == 'true' else False,

                    id_educational_program=item.get("IdEducationalProgram", None),

                    only_for_vo=True if item.get("OnlyForVo", False) == 'true' else False,
                    only_for_spo=True if item.get("OnlyForSpo", False) == 'true' else False,

                    cost_of_study=item.get("CostOfStudy", 0),
                    approved_foiv=True if item.get("ApprovedFoiv", False) == 'true' else False
                )
                for item in competition
            ]
        except Exception as e:
            print(e, "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

        session.add_all(c)
        session.commit()

        return True


def get_all_competition():
    with get_session() as session:
        return session.query(Competition).all()





