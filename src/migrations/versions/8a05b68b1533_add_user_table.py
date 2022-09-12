"""add_user_table

Revision ID: 8a05b68b1533
Revises: 
Create Date: 2022-09-01 21:01:43.082696

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "8a05b68b1533"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("first_name", sa.String(length=255), nullable=True),
        sa.Column("last_name", sa.String(length=255), nullable=True),
        sa.Column("monobank_token", sa.String(length=255), nullable=False),
        sa.Column("created_date", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("monobank_token"),
    )


def downgrade() -> None:
    op.drop_table("user")
