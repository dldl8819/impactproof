"""add source_doc_id unique constraint to work_items

Revision ID: 0002_source_doc_unique
Revises: 0001_init
Create Date: 2026-05-01
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


revision: str = "0002_source_doc_unique"
down_revision: Union[str, None] = "0001_init"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("work_items", sa.Column("source_doc_id", sa.Integer(), nullable=True))

    op.execute(
        """
        UPDATE work_items
        SET source_doc_id = (evidence_json ->> 'source_doc_id')::integer
        WHERE (evidence_json ->> 'source_doc_id') ~ '^[0-9]+$'
        """
    )

    op.alter_column("work_items", "source_doc_id", nullable=False)
    op.create_index("ix_work_items_source_doc_id", "work_items", ["source_doc_id"], unique=True)
    op.create_foreign_key(
        "fk_work_items_source_doc_id_source_docs",
        "work_items",
        "source_docs",
        ["source_doc_id"],
        ["id"],
        ondelete="RESTRICT",
    )


def downgrade() -> None:
    op.drop_constraint("fk_work_items_source_doc_id_source_docs", "work_items", type_="foreignkey")
    op.drop_index("ix_work_items_source_doc_id", table_name="work_items")
    op.drop_column("work_items", "source_doc_id")
