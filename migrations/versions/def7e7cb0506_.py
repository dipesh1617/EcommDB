"""empty message

Revision ID: def7e7cb0506
Revises: 3bf346f90659
Create Date: 2017-04-08 20:04:21.819056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'def7e7cb0506'
down_revision = '3bf346f90659'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personal_info',
    sa.Column('dummy_ID', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=True),
    sa.Column('address', sa.String(length=80), nullable=True),
    sa.Column('city', sa.String(length=10), nullable=True),
    sa.Column('country', sa.String(length=20), nullable=True),
    sa.Column('postal_code', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('passwd', sa.String(length=20), nullable=True),
    sa.Column('login_id', sa.String(length=20), nullable=True),
    sa.Column('customer', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['customer'], ['customer.customer_id'], ),
    sa.PrimaryKeyConstraint('dummy_ID'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('login_id')
    )
    op.drop_table('personalinfo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personalinfo',
    sa.Column('dummy_ID', sa.INTEGER(), server_default=sa.text(u'nextval(\'"personalinfo_dummy_ID_seq"\'::regclass)'), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('country', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('postal_code', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('passwd', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('login_id', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('customer', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['customer'], [u'customer.customer_id'], name=u'personalinfo_customer_fkey'),
    sa.PrimaryKeyConstraint('dummy_ID', name=u'personalinfo_pkey'),
    sa.UniqueConstraint('email', name=u'personalinfo_email_key'),
    sa.UniqueConstraint('login_id', name=u'personalinfo_login_id_key')
    )
    op.drop_table('personal_info')
    # ### end Alembic commands ###
