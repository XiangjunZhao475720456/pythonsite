"""empty message

Revision ID: 6fbfca8a9174
Revises: d78be4a62a1f
Create Date: 2018-02-22 15:41:33.095617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fbfca8a9174'
down_revision = 'd78be4a62a1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('common_user', sa.Column('gender', sa.String(length=1), server_default='女', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('common_user', 'gender')
    # ### end Alembic commands ###
