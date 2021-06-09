"""empty message

Revision ID: 33d45a6d8651
Revises: 737b85598330
Create Date: 2021-05-26 10:39:18.702952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33d45a6d8651'
down_revision = '737b85598330'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clients', sa.Column('avatar_uploaded', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('clients', 'avatar_uploaded')
    # ### end Alembic commands ###
