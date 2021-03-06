"""empty message

Revision ID: 3c51ef93b8c0
Revises: 9ef0fce9744b
Create Date: 2021-09-13 17:31:17.211951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c51ef93b8c0'
down_revision = '9ef0fce9744b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('Todo', sa.Column('list_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Todo', 'todolists', ['list_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Todo', type_='foreignkey')
    op.drop_column('Todo', 'list_id')
    op.drop_table('todolists')
    # ### end Alembic commands ###
