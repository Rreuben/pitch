"""Removed title property from Comment class

Revision ID: 53f4bf4f2a96
Revises: 1ec6a0976fec
Create Date: 2018-09-14 13:23:16.346611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53f4bf4f2a96'
down_revision = '1ec6a0976fec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###