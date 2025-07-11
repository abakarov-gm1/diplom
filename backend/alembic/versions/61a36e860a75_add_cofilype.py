"""add cofilype

Revision ID: 61a36e860a75
Revises: f3311b90e928
Create Date: 2025-06-14 19:26:55.000513

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61a36e860a75'
down_revision: Union[str, None] = 'f3311b90e928'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('competition_group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('competition_id', sa.BigInteger(), nullable=True),
    sa.Column('application_id', sa.BigInteger(), nullable=True),
    sa.Column('direction_id', sa.BigInteger(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.Column('is_ovo', sa.Boolean(), nullable=True),
    sa.Column('education_form_id', sa.Integer(), nullable=True),
    sa.Column('place_type_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('status_competition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('actual', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('status_competition')
    op.drop_table('competition_group')
    # ### end Alembic commands ###
