"""rev2-test

Revision ID: 00980bbee5d2
Revises: 8f86bdf095cb
Create Date: 2022-08-03 19:40:33.540267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00980bbee5d2'
down_revision = '8f86bdf095cb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('citizens', sa.Column('house_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'citizens', 'houses', ['house_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'citizens', type_='foreignkey')
    op.drop_column('citizens', 'house_id')
    # ### end Alembic commands ###
