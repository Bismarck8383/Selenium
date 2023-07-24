"""Add + camps employees

Revision ID: 144efd159825
Revises: 8076b959cec9
Create Date: 2023-07-20 15:45:44.938200

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '144efd159825'
down_revision = '8076b959cec9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('employee', sa.Column('fecha_contratacion', sa.Date(), nullable=True))
    op.add_column('employee', sa.Column('salario', sa.Float(), nullable=True))
    op.add_column('employee', sa.Column('telefono', sa.String(length=15), nullable=True))
    op.add_column('employee', sa.Column('direccion', sa.String(length=100), nullable=True))
    op.add_column('employee', sa.Column('genero', sa.String(length=10), nullable=True))


def downgrade() -> None:
    op.drop_column('employee', 'fecha_contratacion')
    op.drop_column('employee', 'salario')
    op.drop_column('employee', 'telefono')
    op.drop_column('employee', 'direccion')
    op.drop_column('employee', 'genero')
