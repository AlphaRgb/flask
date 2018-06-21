"""add autoincrement

Revision ID: 314dddfea7f7
Revises: 35651f88e26e
Create Date: 2018-06-21 16:49:01.034191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '314dddfea7f7'
down_revision = '35651f88e26e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('chapter_and_novel_id', table_name='chapters')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('chapter_and_novel_id', 'chapters', ['chapter', 'novel_id'], unique=True)
    # ### end Alembic commands ###
