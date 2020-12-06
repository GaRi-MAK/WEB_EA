"""test

Revision ID: d976f370c4ce
Revises: 
Create Date: 2020-12-06 20:54:38.910011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd976f370c4ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cloud_service',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=200), nullable=True),
    sa.Column('even', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contact',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('region', sa.String(length=100), nullable=True),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('flag', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('Events_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Events_title', sa.String(length=100), nullable=True),
    sa.Column('Events_time', sa.String(length=200), nullable=True),
    sa.Column('Events_city', sa.String(length=200), nullable=True),
    sa.Column('Events_country', sa.String(length=200), nullable=True),
    sa.Column('Events_intro', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('Events_id')
    )
    op.create_table('howtobuy',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=240), nullable=True),
    sa.Column('url', sa.String(length=240), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('info_editions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=200), nullable=True),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('main_product',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('intro', sa.String(length=200), nullable=True),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.Column('icon', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('partners_content',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('c_title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=240), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('intro', sa.String(length=200), nullable=True),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('whysql',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('url', sa.String(length=240), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    op.create_table('info_editionsdesc',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=200), nullable=True),
    sa.Column('infoeditions_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['infoeditions_id'], ['info_editions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.create_table('service_type',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=200), nullable=True),
    sa.Column('service_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('whysql_content',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=240), nullable=True),
    sa.Column('whysql_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['whysql_id'], ['whysql.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('whysql_content')
    op.drop_table('service_type')
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_table('info_editionsdesc')
    op.drop_table('followers')
    op.drop_table('whysql')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('service')
    op.drop_table('partners_content')
    op.drop_table('main_product')
    op.drop_table('info_editions')
    op.drop_table('howtobuy')
    op.drop_table('events')
    op.drop_table('contact')
    op.drop_table('cloud_service')
    # ### end Alembic commands ###