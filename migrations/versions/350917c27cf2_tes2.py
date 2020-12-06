"""tes2

Revision ID: 350917c27cf2
Revises: d976f370c4ce
Create Date: 2020-12-06 21:31:45.969467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '350917c27cf2'
down_revision = 'd976f370c4ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('howtobuy',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=240), nullable=True),
    sa.Column('url', sa.String(length=240), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('htb')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('htb',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), nullable=True),
    sa.Column('content', sa.VARCHAR(length=240), nullable=True),
    sa.Column('url', sa.VARCHAR(length=240), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('howtobuy')
    # ### end Alembic commands ###