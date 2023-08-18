"""Fahad Md Kamal Initial migratoin

Revision ID: 6f9d5ebd7d74
Revises: 
Create Date: 2023-08-18 10:02:29.509979

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f9d5ebd7d74'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('publication_date', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('publication_date', sa.DateTime(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('posts')
    # ### end Alembic commands ###
