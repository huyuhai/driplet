"""empty message

Revision ID: 47cda3460b9b
Revises: d1f42d033f0b
Create Date: 2019-02-23 21:05:06.600468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47cda3460b9b'
down_revision = 'd1f42d033f0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.drop_constraint('creator', type_='foreignkey')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'user', ['creator'], ['id'])

    # ### end Alembic commands ###
