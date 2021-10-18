"""Article

Revision ID: 7e8a8167713f
Revises: e9b22f110d46
Create Date: 2021-10-16 21:52:34.178033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e8a8167713f'
down_revision = 'e9b22f110d46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('header', sa.String(length=280), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'header')
    # ### end Alembic commands ###