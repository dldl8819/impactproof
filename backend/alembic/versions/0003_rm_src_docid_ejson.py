"""remove source_doc_id from evidence_json

Revision ID: 0003_rm_src_docid_ejson
Revises: 0002_source_doc_unique
Create Date: 2026-05-01
"""

# NOTE:
# Keep revision id within alembic_version.version_num length constraints
# (commonly VARCHAR(32) in existing environments).

from typing import Sequence, Union

from alembic import op


revision: str = "0003_rm_src_docid_ejson"
down_revision: Union[str, None] = "0002_source_doc_unique"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        UPDATE work_items
        SET evidence_json = (evidence_json::jsonb - 'source_doc_id')::json
        WHERE (evidence_json ->> 'source_doc_id') IS NOT NULL
        """
    )


def downgrade() -> None:
    op.execute(
        """
        UPDATE work_items
        SET evidence_json = (evidence_json::jsonb || jsonb_build_object('source_doc_id', source_doc_id))::json
        WHERE source_doc_id IS NOT NULL
        """
    )
