"""create testimonial table

Revision ID: 61d0bbac6c3a
Revises: 6ffa8f51c21e
Create Date: 2021-10-17 08:16:13.859812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61d0bbac6c3a'
down_revision = '6ffa8f51c21e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'testimonial',
        sa.Column('id', sa.Integer),
        sa.Column('business_id', sa.Integer),
        sa.Column('is_accepted', sa.Boolean),
        sa.Column('giver_name', sa.String),
        sa.Column('giver_title', sa.String),
        sa.Column('business_name', sa.String),
        sa.Column('picture_url', sa.String),
        sa.Column('text', sa.String),
        sa.Column('audio_url', sa.String),
        sa.Column('video_url', sa.String),
        sa.Column('created_on', sa.Integer),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['business_id'], ['business.id'], ondelete='cascade'))

    op.create_index(op.f('ix_testimonial_id'), 'testimonial', ['id'])
    op.create_index(op.f('ix_testimonial_business_name'), 'testimonial', ['business_name'])


def downgrade():
    op.drop_table('testimonial')
