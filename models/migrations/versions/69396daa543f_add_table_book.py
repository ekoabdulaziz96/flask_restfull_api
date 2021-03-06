"""add table book

Revision ID: 69396daa543f
Revises: 1a538303c127
Create Date: 2021-09-29 14:30:23.437074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69396daa543f'
down_revision = '1a538303c127'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###
