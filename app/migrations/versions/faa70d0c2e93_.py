"""empty message

Revision ID: faa70d0c2e93
Revises: 24c9016aa594
Create Date: 2021-08-18 23:04:15.841892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'faa70d0c2e93'
down_revision = '24c9016aa594'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patients_data',
    sa.Column('id_', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('logdate', sa.DateTime(), nullable=True),
    sa.Column('Email', sa.String(), nullable=True),
    sa.Column('Password', sa.LargeBinary(), nullable=True),
    sa.Column('FirstName', sa.String(), nullable=True),
    sa.Column('LastName', sa.String(), nullable=True),
    sa.Column('BMI', sa.Float(), nullable=True),
    sa.Column('Pregnancy', sa.Integer(), nullable=True),
    sa.Column('Age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patients_data')
    # ### end Alembic commands ###
