"""add content column to posts table

Revision ID: f25483dd4d3d
Revises: 08c626ab8462
Create Date: 2023-07-04 11:26:22.433875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f25483dd4d3d'
down_revision = '08c626ab8462'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
