"""add colu filype

Revision ID: 729186f2ea10
Revises: f5631ec9dc61
Create Date: 2025-06-14 12:59:56.138145

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '729186f2ea10'
down_revision: Union[str, None] = 'f5631ec9dc61'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('competitions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.UUID(), nullable=False),
    sa.Column('ogrn_owner_organization', sa.String(length=20), nullable=False),
    sa.Column('kpp_owner_organization', sa.String(length=20), nullable=False),
    sa.Column('id_campaign', sa.Integer(), nullable=False),
    sa.Column('id_direction', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('id_education_level', sa.Integer(), nullable=False),
    sa.Column('id_education_form', sa.Integer(), nullable=False),
    sa.Column('id_place_type', sa.Integer(), nullable=False),
    sa.Column('number_places', sa.Integer(), nullable=False),
    sa.Column('id_stage_admission', sa.Integer(), nullable=False),
    sa.Column('only_for_foreigners', sa.Boolean(), nullable=True),
    sa.Column('only_citizens_rf', sa.Boolean(), nullable=True),
    sa.Column('second_education_arts', sa.Boolean(), nullable=True),
    sa.Column('preview_tours', sa.Boolean(), nullable=True),
    sa.Column('attaching_portfolio', sa.Boolean(), nullable=True),
    sa.Column('medical_examination', sa.Boolean(), nullable=True),
    sa.Column('id_educational_program', sa.Integer(), nullable=True),
    sa.Column('only_for_vo', sa.Boolean(), nullable=True),
    sa.Column('only_for_spo', sa.Boolean(), nullable=True),
    sa.Column('cost_of_study', sa.Integer(), nullable=False),
    sa.Column('approved_foiv', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('competitions')
    # ### end Alembic commands ###
