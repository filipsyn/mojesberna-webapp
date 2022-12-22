"""empty message

Revision ID: 0e6a97787879
Revises: b64726fd3e86
Create Date: 2022-12-22 18:18:36.622737

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0e6a97787879'
down_revision = 'b64726fd3e86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('first_name', sa.String(length=64), nullable=False),
                    sa.Column('last_name', sa.String(length=64), nullable=True),
                    sa.Column('telephone_number', sa.String(length=17), nullable=True),
                    sa.Column('password_hash', sa.String(length=128), nullable=False),
                    sa.Column('address', sa.String(length=255), nullable=True),
                    sa.PrimaryKeyConstraint('user_id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
