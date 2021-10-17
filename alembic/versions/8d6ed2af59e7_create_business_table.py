"""Create business table

Revision ID: 8d6ed2af59e7
Revises:
Create Date: 2021-10-16 14:03:43.265754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d6ed2af59e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'business',
        sa.Column('id', sa.Integer),
        sa.Column('name', sa.String),
        sa.Column('identity', sa.String),
        sa.Column('has_premium', sa.Boolean),
        sa.Column('created_on', sa.Integer),
        sa.PrimaryKeyConstraint('id'))

    op.create_index(op.f('ix_business_id'), 'business', ['id'])
    op.create_index(op.f('ix_business_name'), 'business', ['name'])
    op.create_index(op.f('ix_business_identity'), 'business', ['identity'], unique=True)


def downgrade():
    op.drop_table('business')
