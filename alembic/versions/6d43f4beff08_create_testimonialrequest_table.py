"""create testimonialrequest table

Revision ID: 6d43f4beff08
Revises: 61d0bbac6c3a
Create Date: 2021-10-19 20:08:10.301350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d43f4beff08'
down_revision = '61d0bbac6c3a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'testimonialrequest',
        sa.Column('id', sa.Integer),
        sa.Column('business_id', sa.Integer),
        sa.Column('questions', sa.dialects.postgresql.JSONB),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['business_id'], ['business.id'], ondelete='cascade'))

    op.create_index(op.f('ix_testimonialrequest_id'), 'testimonialrequest', ['id'])


def downgrade():
    op.drop_table('testimonialrequest')
