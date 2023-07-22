"""add content column to posts table

Revision ID: 05896aea111a
Revises: a99ce3b8c37e
Create Date: 2023-07-22 07:57:10.215289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05896aea111a'
down_revision = 'a99ce3b8c37e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
