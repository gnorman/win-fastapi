"""add last few columns to posts table 2

Revision ID: 4cc0743e4a4f
Revises: 6ea8fbe7f32d
Create Date: 2023-07-09 10:05:40.193122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cc0743e4a4f'
down_revision = '6ea8fbe7f32d'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default="TRUE"),) 
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass

