"""empty message

Revision ID: bfe42bbe0f5b
Revises: def7e7cb0506
Create Date: 2017-04-08 20:06:16.131731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfe42bbe0f5b'
down_revision = 'def7e7cb0506'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orderdetails', sa.Column('useless_id', sa.Integer(), nullable=False))
    op.drop_column('orderdetails', 'useless_ID')
    op.add_column('personal_info', sa.Column('dummy_id', sa.String(length=20), nullable=False))
    op.drop_column('personal_info', 'dummy_ID')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('personal_info', sa.Column('dummy_ID', sa.INTEGER(), server_default=sa.text(u'nextval(\'"personal_info_dummy_ID_seq"\'::regclass)'), nullable=False))
    op.drop_column('personal_info', 'dummy_id')
    op.add_column('orderdetails', sa.Column('useless_ID', sa.INTEGER(), server_default=sa.text(u'nextval(\'"orderdetails_useless_ID_seq"\'::regclass)'), nullable=False))
    op.drop_column('orderdetails', 'useless_id')
    # ### end Alembic commands ###
