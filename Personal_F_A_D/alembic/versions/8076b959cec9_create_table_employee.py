"""create table employee

Revision ID: 8076b959cec9
Revises: ff27e943164a
Create Date: 2023-07-19 12:45:02.048535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8076b959cec9'
down_revision = 'ff27e943164a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'employee',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
        sa.Column('ciudad', sa.String(100), nullable=False),
        sa.Column('edad', sa.Integer, nullable=False),
        sa.Column('cargo', sa.String(100), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('employee')

