"""empty message

Revision ID: 61392e0900f1
Revises: 648d73f2eddf
Create Date: 2018-03-12 17:37:57.569713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61392e0900f1'
down_revision = '648d73f2eddf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('common_user', sa.Column('realname', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('common_user', 'realname')
    # ### end Alembic commands ###