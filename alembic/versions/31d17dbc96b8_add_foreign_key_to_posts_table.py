"""add foreign key to posts table

Revision ID: 31d17dbc96b8
Revises: 6cc03891a711
Create Date: 2023-07-22 08:10:21.112889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31d17dbc96b8'
down_revision = '6cc03891a711'
branch_labels = None
depends_on = None

# add foreign key to posts table
def upgrade() -> None:
    op.add_column("posts", sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass

def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
