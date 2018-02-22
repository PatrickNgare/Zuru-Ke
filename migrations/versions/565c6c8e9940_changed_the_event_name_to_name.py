"""Changed the event_name to name

Revision ID: 565c6c8e9940
Revises: 5286ccbbb265
Create Date: 2018-02-16 10:55:39.607684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '565c6c8e9940'
down_revision = '5286ccbbb265'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bookings', sa.Column('name', sa.String(length=255), nullable=True))
    op.drop_column('bookings', 'event_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bookings', sa.Column('event_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('bookings', 'name')
    # ### end Alembic commands ###
