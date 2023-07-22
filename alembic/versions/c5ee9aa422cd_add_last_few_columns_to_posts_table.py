"""add last few columns to posts table

Revision ID: c5ee9aa422cd
Revises: 31d17dbc96b8
Create Date: 2023-07-22 08:19:16.354602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5ee9aa422cd'
down_revision = '31d17dbc96b8'
branch_labels = None
depends_on = None

# add last few columns to post table
def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default="TRUE"),) 
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
