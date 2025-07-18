"""add colu filype

Revision ID: 07922eb1921b
Revises: ed53bd639ad1
Create Date: 2025-06-14 11:45:44.771978

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '07922eb1921b'
down_revision: Union[str, None] = 'ed53bd639ad1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('EducationLevelCls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_level_cls', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('actual', sa.Boolean(), nullable=True),
    sa.Column('education_level_group_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('EducationLevelCls')
    # ### end Alembic commands ###
