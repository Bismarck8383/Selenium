"""table employee

Revision ID: df3bc8061d32
Revises: 
Create Date: 2023-07-19 10:10:57.101119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df3bc8061d32'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'employee',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False),
        sa.Column('ciudad', sa.String(length=100), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('employee')
