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
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, index=True),
        sa.Column('identity', sa.String, unique=True, index=True),
        sa.Column('is_subscribed', sa.Boolean),
        sa.PrimaryKeyConstraint('id'))

    op.create_index(op.f('ix_business_id'), 'business', ['id'], unique=True)
    op.create_index(op.f('ix_business_name'), 'business', ['name'])
    op.create_index(op.f('ix_business_identity'), 'business', ['identity'], unique=True)


def downgrade():
    op.drop_table('business')
