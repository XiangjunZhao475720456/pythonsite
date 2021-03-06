"""empty message

Revision ID: 081e151dcce1
Revises: 0e5708946f68
Create Date: 2018-03-12 20:12:01.638200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '081e151dcce1'
down_revision = '0e5708946f68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('common_user', sa.Column('realname', sa.String(length=64), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('common_user', 'realname')
    # ### end Alembic commands ###
