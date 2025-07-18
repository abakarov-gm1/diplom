"""add cofilype

Revision ID: f3311b90e928
Revises: 729186f2ea10
Create Date: 2025-06-14 13:47:22.761919

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f3311b90e928'
down_revision: Union[str, None] = '729186f2ea10'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('competitions', 'uid',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('competitions', 'ogrn_owner_organization',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('competitions', 'kpp_owner_organization',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('competitions', 'id_campaign',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('competitions', 'id_direction',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('competitions', 'id_education_level',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('competitions', 'id_education_form',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('competitions', 'id_place_type',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('competitions', 'number_places',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('competitions', 'id_stage_admission',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('competitions', 'id_stage_admission',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('competitions', 'number_places',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('competitions', 'id_place_type',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('competitions', 'id_education_form',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('competitions', 'id_education_level',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('competitions', 'id_direction',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('competitions', 'id_campaign',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('competitions', 'kpp_owner_organization',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('competitions', 'ogrn_owner_organization',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('competitions', 'uid',
               existing_type=sa.UUID(),
               nullable=False)
    # ### end Alembic commands ###
