"""
Add a column

Revision ID: 851f2c656dd6
Revises: 2e43bcc65930
Create Date: 2023-07-17 13:11:39.831681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '851f2c656dd6'
down_revision = '2e43bcc65930'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('user', sa.Column('age', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('address', sa.String(length=100), nullable=False))


def downgrade() -> None:
    op.drop_column('user', 'age')
    op.drop_column('user', 'address')
