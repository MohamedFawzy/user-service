"""create_user_table
Revision ID: 7a53064e53df
Revises: 
Create Date: 2021-04-01 15:22:21.927870
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
revision = "7a53064e53df"
down_revision = None
branch_labels = None
depends_on = None

# ###
# win = Column(TINYINT(1, unsigned=True), nullable=False, default=0,
#     server_default=text('0'),
#     unique=True,
# )


def create_user_table() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.VARCHAR, nullable=False),
        sa.Column("last_name", sa.VARCHAR, nullable=False),
        sa.Column("email", sa.VARCHAR, nullable=False, index=True, unique=True),
        sa.Column("password", sa.VARCHAR, nullable=False),
        sa.Column(
            "is_active",
            sa.VARCHAR(1),
            nullable=False,
            index=True,
            default=0,
            server_default=sa.text("0"),
        ),
    )


def upgrade() -> None:
    create_user_table()


def downgrade() -> None:
    op.drop_table("users")
