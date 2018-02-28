"""empty message

Revision ID: 58a302280d3f
Revises: 6fbfca8a9174
Create Date: 2018-02-22 15:42:27.128581

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '58a302280d3f'
down_revision = '6fbfca8a9174'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('common_user', 'gender')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('common_user', sa.Column('gender', mysql.VARCHAR(length=1), server_default=sa.text("'女'"), nullable=False))
    # ### end Alembic commands ###