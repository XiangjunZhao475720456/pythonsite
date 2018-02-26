"""empty message

Revision ID: 99922e432b9b
Revises: d5985d8aa227
Create Date: 2018-02-22 15:36:20.109161

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '99922e432b9b'
down_revision = 'd5985d8aa227'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('email', table_name='common_user')
    op.drop_column('common_user', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('common_user', sa.Column('email', mysql.VARCHAR(length=255), nullable=True))
    op.create_index('email', 'common_user', ['email'], unique=True)
    # ### end Alembic commands ###
