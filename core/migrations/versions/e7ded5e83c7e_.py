"""empty message

Revision ID: e7ded5e83c7e
Revises: 52a401750a76
Create Date: 2024-04-25 23:27:28.201709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7ded5e83c7e'
down_revision = '52a401750a76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('assignments', 'state',
               existing_type=sa.VARCHAR(length=9),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('assignments', 'state',
               existing_type=sa.VARCHAR(length=9),
               nullable=True)
    # ### end Alembic commands ###
