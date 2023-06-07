"""empty message

Revision ID: bef841c08198
Revises: dd219fd64657
Create Date: 2021-08-16 05:13:35.801574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bef841c08198'
down_revision = 'dd219fd64657'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patients_data', 'id_')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patients_data', sa.Column('id_', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###