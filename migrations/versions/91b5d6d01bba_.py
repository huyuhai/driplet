"""empty message

Revision ID: 91b5d6d01bba
Revises: 188347d158f0
Create Date: 2019-02-23 20:41:36.347306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91b5d6d01bba'
down_revision = '188347d158f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todo', type_='foreignkey')
    op.create_foreign_key(None, 'todo', 'user', ['creator'], ['username'])
    op.drop_column('todo', 'creator_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('creator_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'todo', type_='foreignkey')
    op.create_foreign_key(None, 'todo', 'user', ['creator'], ['id'])
    # ### end Alembic commands ###
