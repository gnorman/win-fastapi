"""create posts table

Revision ID: a99ce3b8c37e
Revises: 
Create Date: 2023-07-21 09:38:07.615633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a99ce3b8c37e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass

def downgrade() -> None:
    op.drop_table('posts')
    pass
