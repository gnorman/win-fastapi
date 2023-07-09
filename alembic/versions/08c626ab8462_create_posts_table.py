"""create posts table

Revision ID: 08c626ab8462
Revises: 
Create Date: 2023-07-04 11:03:27.779052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08c626ab8462'
down_revision = None
branch_labels = None
depends_on = None


#def upgrade() -> None:
    #pass


#def downgrade() -> None:
    #pass

def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass

def downgrade():
    op.drop_table('posts')
    pass