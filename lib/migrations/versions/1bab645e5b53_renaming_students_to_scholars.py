"""Renaming students to scholars

Revision ID: 1bab645e5b53
Revises: 791279dd0760
Create Date: 2023-06-01 17:23:49.543243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bab645e5b53'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students','scholars')


def downgrade() -> None:
    op.rename_table('scholars','students')
