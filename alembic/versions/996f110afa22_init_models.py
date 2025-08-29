"""init models"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "996f110afa22"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "questions",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("text", sa.String, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
    )

    op.create_table(
        "answers",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("question_id", sa.Integer, sa.ForeignKey("questions.id", ondelete="CASCADE"), nullable=False),
        sa.Column("user_id", sa.String, nullable=False),
        sa.Column("text", sa.String, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table("answers")
    op.drop_table("questions")

