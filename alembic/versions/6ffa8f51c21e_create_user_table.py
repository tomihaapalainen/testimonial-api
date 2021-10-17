"""Create user table

Revision ID: 6ffa8f51c21e
Revises: 8d6ed2af59e7
Create Date: 2021-10-16 14:08:04.030840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ffa8f51c21e'
down_revision = '8d6ed2af59e7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer),
        sa.Column('business_id', sa.Integer),
        sa.Column('created_on', sa.Integer),
        sa.Column('email', sa.String),
        sa.Column('name', sa.String),
        sa.Column('is_admin', sa.Boolean),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['business_id'], ['business.id'], ondelete='cascade'),
        sa.UniqueConstraint('email'))

    op.create_index(op.f('ix_user_id'), 'user', ['id'])
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)


def downgrade():
    op.drop_table('user')
