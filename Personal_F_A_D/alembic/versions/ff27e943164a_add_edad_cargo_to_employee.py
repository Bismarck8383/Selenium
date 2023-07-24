"""Add edad,cargo to employee

Revision ID: ff27e943164a
Revises: df3bc8061d32
Create Date: 2023-07-19 12:29:21.593392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff27e943164a'
down_revision = 'df3bc8061d32'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('employee', sa.Column('edad', sa.Integer(), nullable=False))
    op.add_column('employee', sa.Column('cargo', sa.String(length=100), nullable=False))


def downgrade() -> None:
    op.drop_column('employee', 'edad')
    op.drop_column('employee', 'cargo')

