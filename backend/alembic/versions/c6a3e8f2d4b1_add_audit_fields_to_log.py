"""add audit fields to Log

Revision ID: c6a3e8f2d4b1
Revises: fc70450c9eb3
Create Date: 2026-06-05 10:00:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


revision: str = "c6a3e8f2d4b1"
down_revision: Union[str, Sequence[str], None] = "fc70450c9eb3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("Log", "account_id", existing_type=sa.Integer(), nullable=True)
    op.add_column("Log", sa.Column("endpoint", sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False, server_default=""))
    op.add_column("Log", sa.Column("method", sqlmodel.sql.sqltypes.AutoString(length=10), nullable=False, server_default=""))
    op.add_column("Log", sa.Column("response_status", sa.Integer(), nullable=False, server_default="200"))
    op.add_column("Log", sa.Column("duration_ms", sa.Float(), nullable=False, server_default="0.0"))
    op.alter_column("Log", "endpoint", server_default=None)
    op.alter_column("Log", "method", server_default=None)
    op.alter_column("Log", "response_status", server_default=None)
    op.alter_column("Log", "duration_ms", server_default=None)


def downgrade() -> None:
    op.drop_column("Log", "duration_ms")
    op.drop_column("Log", "response_status")
    op.drop_column("Log", "method")
    op.drop_column("Log", "endpoint")
    op.alter_column("Log", "account_id", existing_type=sa.Integer(), nullable=False)
