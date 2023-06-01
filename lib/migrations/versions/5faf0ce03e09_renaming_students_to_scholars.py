"""Renaming students to scholars

Revision ID: 5faf0ce03e09
Revises: 1bab645e5b53
Create Date: 2023-06-01 17:40:22.630843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5faf0ce03e09'
down_revision = '1bab645e5b53'
branch_labels = None
depends_on = None


def upgrade() -> None:
     op.rename_table('students', 'scholars')

def downgrade() -> None:
 op.rename_table('scholars', 'students')
