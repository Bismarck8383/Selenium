"""primera

Revision ID: 2e43bcc65930
Revises: 
Create Date: 2023-07-17 09:43:35.127004

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2e43bcc65930'
down_revision = None
branch_labels = None
depends_on = None

"""
Cuando ejecutas el comando alembic upgrade head, 
estás solicitando a Alembic que aplique todas las 
migraciones pendientes en tu base de datos.
"""


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False)
    )


"""
Si ejecutas el comando alembic downgrade base, estás solicitando a Alembic
 que revierta todas las migraciones aplicadas y vuelva a la base inicial.
"""


def downgrade() -> None:
    op.drop_table('user')
